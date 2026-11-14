from unicorn import *
from unicorn.x86_const import *
import os
import sys
import random
from keystone import *
import msvcrt
import datetime
filename="Output.com"
mu = Uc(UC_ARCH_X86, UC_MODE_16)
mu.mem_map(0x0000, 0x110000)
ks = Ks(KS_ARCH_X86, KS_MODE_16)
render_count = 0

def hook_mem_write(uc, access, address, size, value, user_data):
    if 0xB8000 <= address < 0xC0000:
        print(f"\n[VRAM_WRITE] 物理地址: {address:05X}, 写入的值: {value:02X}", flush=True)
        global vram_count
        vram_count += 1
        if vram_count > 10000:
            uc.emu_stop()
vram_count = 0
mu.hook_add(UC_HOOK_MEM_WRITE, hook_mem_write)
def INT(uc,intno,user_data):
    ah = uc.reg_read(UC_X86_REG_AH)
    al = uc.reg_read(UC_X86_REG_AL)
    if intno==0x20:
        uc.emu.stop()
    elif intno==0x21:
        ah=uc.reg_read(UC_X86_REG_AH)
        al=uc.reg_read(UC_X86_REG_AL)
        if ah==0x4c:
            uc.emu.stop()
        elif ah==0x02:
            dl = mu.reg_read(UC_X86_REG_DL)
            if dl == 0x0D:
                print("\r", end="", flush=True)
            elif dl == 0x0A:
                print("\n", end="", flush=True)
            elif 32 <= dl <= 126:
                try:
                    print(bytes([dl]).decode('cp437'), end="", flush=True)
                except:
                    pass
        elif ah == 0x30:
            uc.reg_write(UC_X86_REG_AL, 0x05)
            uc.reg_write(UC_X86_REG_AH, 0x00)
        elif ah == 0x2A:
            now = datetime.datetime.now()
            uc.reg_write(UC_X86_REG_CX, now.year)
            uc.reg_write(UC_X86_REG_DH, now.month)
            uc.reg_write(UC_X86_REG_DL, now.day)
        elif ah == 0x2C:
            now = datetime.datetime.now()
            uc.reg_write(UC_X86_REG_CH, now.hour)
            uc.reg_write(UC_X86_REG_CL, now.minute)
            uc.reg_write(UC_X86_REG_DH, now.second)
        elif ah==0x09:
            dx = mu.reg_read(UC_X86_REG_DX)
            ds = mu.reg_read(UC_X86_REG_DS)
            addr = (ds << 4) + dx
            while True:
                char = mu.mem_read(addr, 1)[0]
                if char == 0x24:
                    break
                if char == 0x0D:
                    print("\r", end="", flush=True)
                elif char == 0x0A:
                    print("\n", end="", flush=True)
                elif 32 <= char <= 126:
                    try:
                        print(bytes([char]).decode('cp437'), end="", flush=True)
                    except:
                        pass
                addr += 1
        elif ah == 0x01:
            import msvcrt
            key = msvcrt.getch()
            if key == b'\r':
                print()
                uc.reg_write(UC_X86_REG_AL, 0x0D)
            else:
                print(key.decode('ascii', 'ignore'), end="", flush=True)
                uc.reg_write(UC_X86_REG_AL, key[0])
        elif ah == 0x0A:
            dx = uc.reg_read(UC_X86_REG_DX)
            ds = uc.reg_read(UC_X86_REG_DS)
            addr = (ds << 4) + dx
            max_len = uc.mem_read(addr, 1)[0] - 1
            user_input = input()[:max_len]
            uc.mem_write(addr + 1, bytes([len(user_input)]))
            uc.mem_write(addr + 2, user_input.encode('ascii'))
            print()
        elif ah == 0x3D:
            print("\n[DOS] Open File Not Implemented yet.")
        elif ah == 0x3E:
            print("\n[DOS] Close File Not Implemented yet.")
        elif ah == 0x4A:
            flags = uc.reg_read(UC_X86_REG_EFLAGS)
            flags &= ~0x1
            uc.reg_write(UC_X86_REG_EFLAGS, flags)
        else:
            raise Exception("UC_ERR_INSN_INVALID")
    elif intno==0x16:
        ah=uc.reg_read(UC_X86_REG_AH)
        al=uc.reg_read(UC_X86_REG_AL)
        if ah==0x00:
            key=msvcrt.getch()
            if key in (b'r',b'\n'):
                uc.reg_write(UC_X86_REG_AL,0x0D)
            else:
                uc.reg_write(UC_X86_REG_AL,key[0])
            uc.reg_write(UC_X86_REG_AH,0x00)
        elif ah==0x01:
            uc.reg_write(UC_X86_REG_EFLAGS)
            if msvcrt.kbhit():
                key=msvcrt.getch()
                flags &= ~0x40
                uc.reg_write(UC_X86_REG_EFLAGS,flags)
                uc.reg_write(UC_X86_REG_AL,key[0]if key !=b'\r' else 0x0D)
            else:
                flags |= 0x40
                uc.reg_write(UC_X86_REG_EFLAGS,flags)
    elif intno == 0x10:
        ah = mu.reg_read(UC_X86_REG_AH)
        al = mu.reg_read(UC_X86_REG_AL)
    
        if ah == 0x0E: 
            al=mu.reg_read(UC_X86_REG_AL)
            try:
                char=bytes([al]).decode('cp437')
                print(char,end="",flush=True)
            except:
                pass
        
        elif ah == 0x02:
            dh = mu.reg_read(UC_X86_REG_DH) 
            dl = mu.reg_read(UC_X86_REG_DL) 
            print(f"\033[{dh+1};{dl+1}H", end="", flush=True)
        
        elif ah == 0x06:
            if al == 0x00:
                print("\033[2J\033[H", end="", flush=True)
mu.hook_add(UC_HOOK_INTR,INT)
random_cs = random.randint(0x0000, 0x0FFF) 
mu.reg_write(UC_X86_REG_CS, random_cs)
mu.reg_write(UC_X86_REG_IP, 0x0100)

while True:
    print("-", end="", flush=True)
    try:
        command = input().strip()
    except KeyboardInterrupt:
        break
        
    if command == "q":
        break
        
    elif command.startswith("r"):
        parts = command.split()
        if len(parts) == 1:
            ax = mu.reg_read(UC_X86_REG_AX)
            bx = mu.reg_read(UC_X86_REG_BX)
            cx = mu.reg_read(UC_X86_REG_CX)
            dx = mu.reg_read(UC_X86_REG_DX)
            sp = mu.reg_read(UC_X86_REG_SP)
            bp = mu.reg_read(UC_X86_REG_BP)
            si = mu.reg_read(UC_X86_REG_SI)
            di = mu.reg_read(UC_X86_REG_DI)
    
            ds = mu.reg_read(UC_X86_REG_DS)
            es = mu.reg_read(UC_X86_REG_ES)
            ss = mu.reg_read(UC_X86_REG_SS)
            cs = mu.reg_read(UC_X86_REG_CS)
            ip = mu.reg_read(UC_X86_REG_IP)
    
            flags = mu.reg_read(UC_X86_REG_EFLAGS)
            f_str = ""
            f_str += "OV " if flags & 0x800 else "NV "
            f_str += "DN " if flags & 0x400 else "UP "
            f_str += "EI " if flags & 0x200 else "DI "
            f_str += "PL " if flags & 0x80 else "NG "
            f_str += "ZR " if flags & 0x40 else "NZ "
            f_str += "AC " if flags & 0x10 else "NA "
            f_str += "PE " if flags & 0x4 else "PO "
            f_str += "CY " if flags & 0x1 else "NC"

            print(f"AX={ax:04X}  BX={bx:04X}  CX={cx:04X}  DX={dx:04X}  SP={sp:04X}  BP={bp:04X}  SI={si:04X}  DI={di:04X}")
            print(f"DS={ds:04X}  ES={es:04X}  SS={ss:04X}  CS={cs:04X}  IP={ip:04X}  {f_str}")
            try:
                physical_addr = (cs << 4) + ip
                opcode_bytes = mu.mem_read(physical_addr, 3)
                hex_str = " ".join(f"{b:02X}" for b in opcode_bytes)
                print(f"{cs:04X}:{ip:04X}  {hex_str}")
            except UcError:
                print(f"{cs:04X}:{ip:04X}  <Read Error>")
    
        elif len(parts) >= 2:
            reg_name = parts[1].upper()
    
            reg_map = {
                "AX": UC_X86_REG_AX, "BX": UC_X86_REG_BX, 
                "CX": UC_X86_REG_CX, "DX": UC_X86_REG_DX,
                "SP": UC_X86_REG_SP, "BP": UC_X86_REG_BP, 
                "SI": UC_X86_REG_SI, "DI": UC_X86_REG_DI,
                "DS": UC_X86_REG_DS, "ES": UC_X86_REG_ES, 
                "SS": UC_X86_REG_SS, "CS": UC_X86_REG_CS,
                "IP": UC_X86_REG_IP
            }
    
            if reg_name in reg_map:
                if len(parts) >= 3:
                    try:
                        new_val = int(parts[2], 16)
                        mu.reg_write(reg_map[reg_name], new_val)
                    except ValueError:
                        print("Invalid value")
                else:
                    current_val = mu.reg_read(reg_map[reg_name])
                    try:
                        new_val_str = input(f"{reg_name} {current_val:04X}: ")
                        if new_val_str:
                            new_val = int(new_val_str, 16)
                            mu.reg_write(reg_map[reg_name], new_val)
                    except ValueError:
                        print("Invalid value")
                    except KeyboardInterrupt:
                        print()
            else:
                print("Invalid register")
    elif command.startswith("a"):
        parts = command.split()
        cs_val = mu.reg_read(UC_X86_REG_CS)
        if len(parts) > 1:
            try:
                addr = int(parts[1], 16)
            except ValueError:
                print("Invalid address")
                continue
        else:
            addr = mu.reg_read(UC_X86_REG_IP)

        while True:
            try:
                asm_str = input(f"{cs_val:04X}:{addr:04X} ")
            except KeyboardInterrupt:
                print()
                break
        
            if not asm_str:
                break
            asm_str = asm_str.upper()

            try:
                encoding, count = ks.asm(asm_str)
                if not encoding:
                    print("         ^ Error")
                    continue

                code = bytes(encoding)
                physical_addr = (cs_val << 4) + addr
                if physical_addr + len(code) > 0x110000:
                    print("Error: Out of memory bounds!")
                    continue
                
                mu.mem_write(physical_addr, code)
                addr += len(code)

            except Exception as e:
                print(f"^ Error: {e}")
    elif command == "g":
        cs_val = mu.reg_read(UC_X86_REG_CS)
        ip_val = mu.reg_read(UC_X86_REG_IP)
        physical_start = (cs_val << 4) + ip_val
        try:
            mu.emu_start(physical_start, 0x110000)
            print("\nProgram terminated normally.")
            mu.reg_write(UC_X86_REG_CS, cs_val)
            mu.reg_write(UC_X86_REG_IP, 0x0100)
            mu.reg_write(UC_X86_REG_SP, 0xFFFE)
        
        except Exception as e:
            cs = mu.reg_read(UC_X86_REG_CS)
            ip = mu.reg_read(UC_X86_REG_IP)
            ax = mu.reg_read(UC_X86_REG_AX)
            bx = mu.reg_read(UC_X86_REG_BX)
            cx = mu.reg_read(UC_X86_REG_CX)
            dx = mu.reg_read(UC_X86_REG_DX)
            sp = mu.reg_read(UC_X86_REG_SP)
            bp = mu.reg_read(UC_X86_REG_BP)
            si = mu.reg_read(UC_X86_REG_SI)
            di = mu.reg_read(UC_X86_REG_DI)
            ds = mu.reg_read(UC_X86_REG_DS)
            es = mu.reg_read(UC_X86_REG_ES)
            ss = mu.reg_read(UC_X86_REG_SS)
            flags = mu.reg_read(UC_X86_REG_EFLAGS)
        
            f_str = ""
            f_str += "OV " if flags & 0x800 else "NV "
            f_str += "DN " if flags & 0x400 else "UP "
            f_str += "EI " if flags & 0x200 else "DI "
            f_str += "PL " if flags & 0x80 else "NG "
            f_str += "ZR " if flags & 0x40 else "NZ "
            f_str += "AC " if flags & 0x10 else "NA "
            f_str += "PE " if flags & 0x4 else "PO "
            f_str += "CY " if flags & 0x1 else "NC"

            err_str = str(e).upper()
            if "DIVIDE" in err_str or "ZERO" in err_str:
                err_code = "00"
            elif "INVALID" in err_str or "INSN" in err_str:
                err_code = "06"
            elif "UNMAPPED" in err_str or "FETCH" in err_str or "READ" in err_str or "WRITE" in err_str:
                err_code = "0E"
            else:
                err_code = "0D"

            try:
                physical_addr = (cs << 4) + ip
                crash_bytes = mu.mem_read(physical_addr, 6)
                hex_codes = " ".join(f"{b:02X}" for b in crash_bytes)
            except Exception:
                hex_codes = "OUT_OF_BOUNDS"

            print(f"\nJemmEx: exception {err_code} occurred at CS:EIP={cs:04X}:{ip:08X}, ERRC=00000000")
            print(f"AX={ax:04X}  BX={bx:04X}  CX={cx:04X}  DX={dx:04X}  SP={sp:04X}  BP={bp:04X}  SI={si:04X}  DI={di:04X}")
            print(f"DS={ds:04X}  ES={es:04X}  SS={ss:04X}  CS={cs:04X}  IP={ip:04X}  {f_str}")
            print(f"[CS:IP]={hex_codes}")
        
            print("Press ESC to abort program...",end="",flush=True)
            import msvcrt
            while True:
                if msvcrt.kbhit():
                    if msvcrt.getch() == b'\x1b':
                        break
        
            mu.reg_write(UC_X86_REG_CS, cs_val)
            mu.reg_write(UC_X86_REG_IP, 0x0100)
            mu.reg_write(UC_X86_REG_SP, 0xFFFE)
            print()
    elif command == "w":
        try:
            cs_val = mu.reg_read(UC_X86_REG_CS)
            ip_val = mu.reg_read(UC_X86_REG_IP)
            physical_addr = (cs_val << 4) + ip_val
        
            try:
                data = mu.mem_read(physical_addr, 100)
            except UcError:
                data = b""
            
            with open(filename, "wb") as f:
                if data:
                    f.write(data)
                
            print(f"Writing {len(data)} bytes")
        
        except Exception:
            print("Write Error")
    elif command.startswith("n"):
        parts = command.split(maxsplit=1)
        if len(parts) == 2:
            filename = parts[1].strip()
            print(f"Name set to [{filename}]")
        else:
            filename = ""
            print("Name cleared")
    elif command.startswith("l"):
        if not filename:
            print("No file specified. Use 'n <filename>' first.")
            continue
        try:
            with open(filename, "rb") as f:
                data = f.read()
            if not data:
                print("File is empty.")
                continue
            cs_val = mu.reg_read(UC_X86_REG_CS)
            physical_start = (cs_val << 4) + 0x0100
            mu.mem_write((cs_val << 4),b'\x00'*0x10000)
            mu.mem_write(physical_start, data)
            mu.reg_write(UC_X86_REG_DS, cs_val)
            mu.reg_write(UC_X86_REG_ES, cs_val)
            mu.mem_write((cs_val << 4) + 0x0080, b'\x00')
            mu.mem_write((cs_val << 4) + 0x0081, b'\x0D')
            mu.reg_write(UC_X86_REG_SS, cs_val)
            mu.reg_write(UC_X86_REG_SP, 0xFFFE)
            mu.reg_write(UC_X86_REG_IP, 0x0100)
            print(f"Loaded {len(data)} bytes from {filename}")
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"Load error: {e}")