#FFFF:0000
import time
import os
import platform
import subprocess
import msvcrt
print("Power on,Self-Test")
time.sleep(1)
print("\033c")
info={}
info['cpu']=platform.processor()or"Unknown CPU"
info['arch']=platform.machine()
print(f"Host Processor    :{info['cpu']}")
print(f"Host arch    :{info['arch']}")
for i in range(0, 2097152 + 1, 256): 
    print(f"\rMemory Test        :{i}K  ", end="", flush=True)
    time.sleep(0.002)
print("[done]")
time.sleep(1)
print('')
time.sleep(1)
print("Detecting IDE Primary Master  ... ST0145224922596")
print("Detecting IDE Primary Slave   ... None")
time.sleep(0.3)
print("start BOOT.MBR to load system")
print("\033c")
try:
    if os.path.exists("boot.mbr"):
        ruturn=subprocess.run(['call','boot.mbr'])
    else:
        print("Boot Failure:boot.mbr is not found")
except:
    print("Boot Failure:boot.mbr is corrupted")
    while True:
        if msvcrt.getch():
            print("Boot Failed,boot.mbr is not found")

