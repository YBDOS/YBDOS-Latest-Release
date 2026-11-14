from dis import Instruction
from re import I
import subprocess as cmd
import ctypes
from ctypes import wintypes
import os
import zipfile
import time
from fs import open_fs
import signal
import sys
from fs.zipfs import ZipFS
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 
import msvcrt
from fs.copy import copy_file
import random
import winsound
import tempfile
import shutil
from fs.copy import copy_file
import fs.osfs
import threading
DRIVE="C:"
VirtualPath={"A:":"A:\\","B:":"B:\\","C:":os.getcwd(),"D:":"D:\\","E:":"E:\\","F:":"F:\\","G:":"G:\\","H:":"H:\\","I:":"I:\\","J:":"J:\\","K:":"K:\\","L:":"L:\\","M:":"M:\\","N:":"N:\\","O:":"O:\\","P:":"P:\\","Q:":"Q:\\","R:":"R:\\","S:":"S:\\","T:":"T:\\","U:":"U:\\","V:":"V:\\","W:":"W:\\","X:":"X:\\","Y:":"Y:\\","Z:":"Z:\\"}
DisplayPath={"A:":"A:\\","B:":"B:\\","C:":"C:\\","D:":"D:\\","E:":"E:\\","F:":"F:\\","G:":"G:\\","H:":"H:\\","I:":"I:\\","J:":"J:\\","K:":"K:\\","L:":"L:\\","M:":"M:\\","N:":"N:\\","O:":"O:\\","P:":"P:\\","Q:":"Q:\\","R:":"R:\\","S:":"S:\\","T:":"T:\\","U:":"U:\\","V:":"V:\\","W:":"W:\\","X:":"X:\\","Y:":"Y:\\","Z:":"Z:\\"}
start_time = time.time()
t = time.localtime()
year = t.tm_year
month = t.tm_mon
day = t.tm_mday
hour = t.tm_hour
minutes = t.tm_min
second = t.tm_sec
warnings.filterwarnings("ignore", category=UserWarning) 
part1=format(random.randint(0x1000,0xffff),"04x")
part2=format(random.randint(0x1000,0xffff),"04x")
C_Volume=str(part1)+"-"+str(part2)
Volume_Serial={"A:":"","B:":"","C:":C_Volume.upper(),"D:":"","E:":"","F:":"","G:":"","H:":"","I:":"","J:":"","K:":"","L:":"","M:":"","N:":"","O:":"","P:":"","Q:":"","R:":"","S:":"","T:":"","U:":"","V:":"","W:":"","X:":"","Y:":"","Z:":""}
InsertDiskPath={"A:":"","B:":"","C:":os.getcwd(),"D:":"","E:":"","F:":"","G:":"","H:":"","I:":"","J:":"","K:":"","L:":"","M:":"","N:":"","O:":"","P:":"","Q:":"","R:":"","S:":"","T:":"","U:":"","V:":"","W:":"","X:":"","Y:":"","Z:":""}
ranslator={"00000000":"STP#","00000001":"#","00000010":"PUT","00000011":"IN","00000100":"OUT","00000101":"SET","00000110":"ADD","00000111":"SUB","00001000":"INC","00001001":"DEC"}
runmem=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
        ]
def output_to_terminal(Output= None):
    print(Output)
def clear_terminal():
    print("\033c")
def pause():
    time.sleep(1)
def cal_time():
    global year, month, day, hour, minutes, second
    now_time = time.time() - start_time

    year += now_time // 31104000
    now_time = now_time % 31104000

    month += now_time // 2592000
    now_time = now_time % 2592000

    day += now_time // 86400
    now_time = now_time % 86400

    hour += now_time // 3600
    now_time = now_time % 3600

    minutes += now_time // 60
    now_time = now_time % 60

    second += now_time

    if second >= 60:
        second -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        hour += 1
    if hour >= 24:
        hour -= 24
        day += 1
    if day > 30:
        day -= 30
        month += 1
    if month > 12:
        month -= 12
        year += 1


    print(f"{int(year)}-{int(month):02d}-{int(day):02d} {int(hour):02d}:{int(minutes):02d}:{second:05.2f}")
def show_start_time():
    print(start_time)
def read_com(filename):
    try:
        with open(filename,"rb")as f:
            Head=f.read(3)
            if Head == b"MQ ":
                move_code_to_mem(filename)
        
    except:
        print("ReadFail")
        print("Read File is broken or file not exist")
def move_code_to_mem(file):
    try:   
        with open(file,"rb")as prg:
            program=prg.read()
            codelength=len(program)
            temp=3
            for i in range(codelength):
                BIN=format(int(program[i]),"08b")
                for j in range(8):
                    runmem[i][j]=int(BIN[j])
                    temp+=1
        print(runmem)
    except:
        print("Error:Can't move to memory,please wait to update and fix it.")
def INSERT_DISK(file,ARG):
    if len(ARG) < 2:
        if ARG.upper()=="A" or "B":
            print(f"Insert {ARG}: in the drive")
            print("Press any key when ready...")
            msvcrt.getch()
            if not os.path.exists(file):
                rt=INT24_ERROR(DRIVE)
                if rt=="abort":
                    return
                elif rt=="retry":
                    INSERT_DISK(file,ARG)
                elif rt=="fail":
                    return
            else:
                InsertDiskPath[ARG]=file
        else:
            if os.path.exists(file):
                InsertDiskPath[str(ARG)+":"]=file
                print(f"Disk {ARG}: is ready")
            else:
                print("Insert Fail:Insert disk is not ready or disk error")
    temppart1=part1=format(random.randint(0x1000,0xffff),"04x")
    temppart2=format(random.randint(0x1000,0xffff),"04x")
    Volume_Serial[str(ARG)+":"]=(str(temppart1)+"-"+str(temppart2)).upper
def do_dir(command, DRIVE, InsertDiskPath, Volume_Serial, VirtualPath, DisplayPath):
    parts = command.split()
    show_page = False
    show_sub = False
    
    target_drive = str(DRIVE).upper()
    if not target_drive.endswith(":"): target_drive += ":"
        
    for arg in parts[1:]:
        arg_upper = arg.upper()
        if "/P" in arg_upper: show_page = True
        if "/S" in arg_upper: show_sub = True
        elif len(arg_upper) == 2 and arg_upper.endswith(":"): target_drive = arg_upper
        
    real_target = VirtualPath.get(target_drive)
    if not real_target:
        real_target = VirtualPath.get(target_drive.replace(":", ""))
        
    if not real_target:
        print(" Invalid drive specification")
        return
        
    display_target = DisplayPath.get(target_drive)
    if not display_target:
        display_target = DisplayPath.get(target_drive.replace(":", ""), f"{target_drive}\\")
        
    vol_info = Volume_Serial.get(target_drive, {})
    if isinstance(vol_info, dict):
        label = vol_info.get("label", "")
        serial = vol_info.get("serial", "0000-0000")
    elif isinstance(vol_info, str):
        label = ""
        serial = vol_info
    else:
        label = ""
        serial = "0000-0000"
    
    if label:
        print(f"Volume in drive {target_drive[0]} is {label}")
    else:
        print(f"Volume in drive {target_drive[0]} has no label")
    print(f"Volume Serial Number is {serial}")
    
    if not show_sub:
        print(f"\n Directory of {display_target}")
        print() 
        
    try:
        line_count = 0
        total_files = 0
        total_dirs = 0
        
        mount_root = InsertDiskPath.get(target_drive) or InsertDiskPath.get(target_drive.replace(":", ""))
        is_zip = False
        if mount_root and str(mount_root).lower().endswith(".zip"):
            is_zip = True

        def format_dos_name(name):
            name = name.upper()
            if "." in name:
                base, ext = name.rsplit(".", 1)
                return f"{base[:8]}.{ext[:3]}"
            return name[:11]

        def print_item(name, is_dir, size=0, mtime=0):
            nonlocal line_count, total_files, total_dirs
            display_name = format_dos_name(name)
            if mtime:
                t = time.localtime(mtime)
                year = str(t.tm_year)[-2:]
                date_str = f"{year}-{t.tm_mon:02d}-{t.tm_mday:02d}"
                hour = t.tm_hour
                ampm = 'a' if hour < 12 else 'p'
                hour = hour if 1 <= hour <= 12 else (hour - 12 if hour > 12 else 12)
                datetime_str = f"{date_str}  {hour:02d}:{t.tm_min:02d}{ampm}"
            else:
                datetime_str = ""

            if is_dir:
                print(f" {display_name:<12} <DIR>         {datetime_str}")
                total_dirs += 1
            else:
                print(f" {display_name:<12} {size:>9}  {datetime_str}")
                total_files += 1
            
            line_count += 1
            if show_page and line_count >= 23:
                print("\n Press any key to continue . . .", end="", flush=True)
                msvcrt.getch() 
                print("\r" + " " * 40 + "\r", end="") 
                line_count = 0

        if is_zip:
            zip_prefix = real_target.replace(mount_root, "").replace("\\", "/").strip("/")
            search_path = f"/{zip_prefix}" if zip_prefix else "/"
            
            zip_fs = open_fs(f"zip://{mount_root}")
            
            if not zip_fs.exists(search_path):
                print(" File Not Found")
                return

            if show_sub:
                for path, dirs, files in zip_fs.walk(search_path):
                    if path != "/":
                        print(f"\n Directory of {target_drive}{path.replace('/', '\\')}")
                    for d in dirs: print_item(d, True)
                    for f in files: print_item(f, False, random.randint(1024, 65536))
            else:
                for f in zip_fs.listdir(search_path):
                    full_f = f"{search_path}/{f}".replace("//", "/")
                    if zip_fs.isdir(full_f): print_item(f, True)
                    else: print_item(f, False, random.randint(1024, 65536))
                    
        else:
            if not os.path.exists(real_target):
                print(" File Not Found")
                return

            if show_sub:
                for root, dirs, files in os.walk(real_target):
                    display_root = root.replace(real_target, display_target)
                    if display_root != display_target:
                        print(f"\n Directory of {display_root}")
                    for d in dirs: 
                        print_item(d, True, mtime=os.path.getmtime(os.path.join(root, d)))
                    for f in files: 
                        f_path = os.path.join(root, f)
                        print_item(f, False, os.path.getsize(f_path), mtime=os.path.getmtime(f_path))
            else:
                for f in os.listdir(real_target):
                    full_f = os.path.join(real_target, f)
                    if os.path.isdir(full_f): 
                        print_item(f, True, mtime=os.path.getmtime(full_f))
                    else: 
                        print_item(f, False, os.path.getsize(full_f), mtime=os.path.getmtime(full_f))
                    
        print(f"\n Total files listed:")
        print(f"               {total_files:>5} File(s)")
        print(f"               {total_dirs:>5} Dir(s)")
        
    except Exception as e:
        print(f"\nRead Error: {e}")
def run_mem_code():
    pass
def System_DIED():
    def ignore_interrupt(signum, frame):
        pass

    signal.signal(signal.SIGINT, ignore_interrupt)
    signal.signal(signal.SIGTERM, ignore_interrupt)    
    while True:
        time.sleep(3600)
def run_floppy_program(exe_name):
    global A_DRIVE_PATH
    
    while True: 
        if not A_DRIVE_PATH:
            choice = INT24_ERROR("A")
            if choice == "retry":
                continue 
            else:
                return 
                
        print(f"\nReading disk A: ", end="", flush=True)
        stop_spinner = threading.Event()
        
        def spin():
            chars = ['-', '\\', '|', '/']
            i = 0
            while not stop_spinner.is_set():
                sys.stdout.write(f"\rReading disk A: {chars[i % 4]}")
                sys.stdout.flush()
                i += 1
                time.sleep(1.0) 
                
        spinner_thread = threading.Thread(target=spin)
        spinner_thread.start()
        
        time.sleep(2.5) 
        
        try:
            if A_DRIVE_PATH.lower().endswith(".zip"):
                zip_fs = open_fs(f"zip://{A_DRIVE_PATH}")
                zip_path = exe_name.replace("\\", "/")
                
                if not zip_fs.exists(zip_path):
                    stop_spinner.set()
                    spinner_thread.join()
                    sys.stdout.write("\r" + " " * 30 + "\r")
                    print("Bad command or file name")
                    return 
                    
                temp_dir = tempfile.mkdtemp(prefix="YBDOS_TEMP_")
                temp_exe = os.path.join(temp_dir, os.path.basename(exe_name))
                
                copy_file(zip_fs, zip_path, fs.osfs.OSFS('/'), temp_exe)
                
                stop_spinner.set()
                spinner_thread.join()
                sys.stdout.write("\r" + " " * 30 + "\r")
                
                print(f"Executing {exe_name}...")
                cmd.run([temp_exe], shell=True)
                
                shutil.rmtree(temp_dir)
                break 
                
            else:
                full_path = os.path.join(A_DRIVE_PATH, exe_name)
                if os.path.exists(full_path):
                    stop_spinner.set()
                    spinner_thread.join()
                    sys.stdout.write("\r" + " " * 30 + "\r")
                    
                    print(f"Executing {exe_name}...")
                    cmd.run([full_path], shell=True)
                    break 
                else:
                    stop_spinner.set()
                    spinner_thread.join()
                    sys.stdout.write("\r" + " " * 30 + "\r")
                    print("Bad command or file name")
                    return
                    
        except Exception:
            stop_spinner.set()
            spinner_thread.join()
            sys.stdout.write("\r" + " " * 30 + "\r")
            
            choice = INT24_ERROR("A")
            if choice == "retry":
                continue 
            else:
                return
def do_cd(command, current_drive, VirtualPath, DisplayPath, InsertDiskPath):
    parts = command.split(maxsplit=1)
    if len(parts) < 2:
        return
        
    target = parts[1].strip()
    base_path = VirtualPath.get(current_drive)
    current_display = DisplayPath.get(current_drive, f"{current_drive}\\")
    real_mount = InsertDiskPath.get(current_drive)
    
    if not base_path:
        return
        
    if target == "..":
        clean_base = base_path.rstrip("\\/")
        new_path = os.path.dirname(clean_base)
        if len(new_path) >= 3:
            VirtualPath[current_drive] = new_path
        else:
            VirtualPath[current_drive] = os.path.splitdrive(clean_base)[0] + "\\"
            
        new_display = os.path.dirname(current_display.rstrip("\\/"))
        if len(new_display) >= 2:
            DisplayPath[current_drive] = new_display
        else:
            DisplayPath[current_drive] = f"{current_drive}\\"
        return
        
    elif target in ["\\", "/"]:
        VirtualPath[current_drive] = os.path.splitdrive(base_path)[0] + "\\"
        DisplayPath[current_drive] = f"{current_drive}\\"
        return
        
    new_path = os.path.join(base_path, target)
    new_display = os.path.join(current_display, target)
    
    if real_mount and real_mount.lower().endswith(".zip"):
        try:
            with zipfile.ZipFile(real_mount, 'r') as z:
                zip_prefix = base_path.replace(f"{current_drive}\\", "").replace("\\", "/").strip("/")
                zip_target = target.replace("\\", "/").strip("/")
                
                if zip_prefix:
                    full_zip_path = f"{zip_prefix}/{zip_target}/"
                else:
                    full_zip_path = f"{zip_target}/"
                
                if any(name.startswith(full_zip_path) for name in z.namelist()):
                    VirtualPath[current_drive] = new_path
                    DisplayPath[current_drive] = new_display
                else:
                    print("The system cannot find the path specified.")
        except Exception:
            print("Zip read error.")
    else:
        if os.path.exists(new_path) and os.path.isdir(new_path):
            VirtualPath[current_drive] = new_path
            DisplayPath[current_drive] = new_display
        else:
            print("The system cannot find the path specified.")
def do_copy(command, current_drive, insert_disk_path):
    parts = command.split()
    if len(parts) < 3:
        return
        
    src_file = parts[1]
    dst_file = parts[2]
    base_path = insert_disk_path.get(current_drive)
    
    if not base_path:
        return
        
    full_src = os.path.join(base_path, src_file)
    full_dst = os.path.join(base_path, dst_file)
    
    if not os.path.exists(full_src) or os.path.isdir(full_src):
        return
        
    try:
        shutil.copyfile(full_src, full_dst)
    except Exception:
        pass
import os
import shutil

def do_copy(command, current_drive, InsertDiskPath):
    parts = command.split()
    if len(parts) < 3:
        return
        
    src_file = parts[1]
    dst_file = parts[2]
    base_path = InsertDiskPath.get(current_drive)
    
    if not base_path:
        return
        
    full_src = os.path.join(base_path, src_file)
    full_dst = os.path.join(base_path, dst_file)
    
    if not os.path.exists(full_src) or os.path.isdir(full_src):
        print("File not found")
        return
        
    try:
        shutil.copyfile(full_src, full_dst)
    except Exception:
        pass
def INT24_ERROR(drive):
    print(f"Not ready reading drive {drive.upper()}")
    RT=choice()
    if RT==1:
        return "abort"
    elif RT==2:
        return "retry"
    elif RT==3:
        return "fail"
def INT0D_ERROR():
    print(f"Not ready reading file.")
    RT=choice()
    if RT==1:
        return "abort"
    elif RT==2:
        return "retry"
    elif RT==3:
        return "fail"
def choice():
    import msvcrt
    print("(A)bort, (R)etry, (F)ail? ", end="", flush=True)
    
    while True:
        lst=['A', 'R', 'F']
        key = msvcrt.getch().decode('utf-8', errors='ignore').upper()
        if key in ['A', 'R', 'F']:
            print(key)
            return (lst.index(key))+1
        else:
            winsound.Beep(825, 100)

