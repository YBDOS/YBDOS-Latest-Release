import os
import winsound
import msvcrt
from tkinter import messagebox
import subprocess as cmd
from colorama import init, Fore, Style
import glob
init(autoreset=True)
from Syntax import *
import time
while True:
    PATH=DisplayPath.get(DRIVE).upper()
    command = input(rf"{PATH}>")
    if command.startswith("cls"):
        clear_terminal()
    elif command.startswith("echo "):
        output_to_terminal(command[5:])
    elif command.startswith("shutdown"):
        print("Performing action: POWEROFF")
        time.sleep(1)
        print("No APM BIOS, trying ACPI",end="")
        for i in range(3):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print("\nTurning OFF system",end="")
        for i in range(3):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print("\nCalling int28 so MSCLIENT can flush",end="")
        for i in range(3):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print("\nResetting DOS filesystem and BIOS disk handler",end="")
        for i in range(3):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print("done.")
        print("Giving disk handlers some time",end="")
        for i in range(3):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print(" Spinning down",end="")
        for i in range(6):
            time.sleep(1)
            print(".",end="",flush=True)
        time.sleep(0.5)
        print("Disks stopped.")
        time.sleep(1)
        print("ACPI mode codes from DSDT: S1 (sleep) is 1/0, S5 (soft-off) is 7/0.")
        time.sleep(0.2)
        print("ACPI for 'PTLTD ' found: FINGROVE, port base 0x400, DSDT size 0xC246.")
        print("FACP@767FEC1E DSDT@767E3000 FACS@7679CFC0 control@404/0 status@400/0")
        exit()
    elif command.lower().startswith("time"):
        cal_time()
    elif command.lower() == "output var:start_time": 
        show_start_time()
    elif command == "":
        pass
    elif command.lower().startswith("beep"):
        winsound.Beep(1000,300)
    elif command == "":
        pass
    elif command.lower().startswith("choice"):
        os.system("choice")
    elif command.startswith("cd "):
        do_cd(command, DRIVE, VirtualPath,DisplayPath,InsertDiskPath)
    elif command.startswith("copy "):
        do_copy(command,DRIVE,InsertDiskPath)
    elif command.startswith("run "):
        lst=command.split()
        run_floppy_program(lst[1])
    elif command == "edit":
        os.system("start edit")
    elif command.startswith("edit "):
        file=command[5:]
        os.system("start edit "+ file)
    elif command.lower()=="debug" or command.lower().startswith("debug "):
        if command!="debug":
            filename=command[6:]

    elif command == "RUN BUG HIGH":
        import random

        while True:
            line = []
            for _ in range(256):
                if random.random() < 0.5:
                    c = random.randint(0x20, 0x7E)
                else:
                    c = random.randint(0xA0, 0x024F)
                line.append(chr(c))
            print("".join(line))
            if msvcrt.kbhit():
                msvcrt.getch()
                winsound.Beep(523, 500)

    else:
        if os.path.isfile(command):
            try:
                if command.endswith(".py"):
                    os.system("python "+command)
                else:
                    os.system("start "+command)
            except:
                INT0D_ERROR()
        elif command.endswith(":") and len(command)==2:
            def program():
                drived=InsertDiskPath.get(command)
                if drived=="" and command == "A:" or command=="B:":
                    rt=INT24_ERROR(command)
                    if rt=="retry":
                        program()
                elif drived=="":
                    print("Invalid drive specification.")
                else:
                    DRIVE=command
            program()
        elif command == "dir" or command.startswith("dir "):
            do_dir(command, DRIVE, InsertDiskPath, Volume_Serial, VirtualPath,DisplayPath)
        elif command.startswith("InsertDisk "):
            Part=command.split()
            ARG=Part[1]
            PATH=Part[2]
            INSERT_DISK(PATH,ARG)
        else:
            parts = command.split()
            print("bad command or file name")