import os
import pyfiglet
if os.path.exists("config.bat"):
    os.system("config.bat")
else:
    boot=pyfiglet.figlet_format("boot",font='slant')
    print("Welcome to boot.mbr")
    while True:
        filepath=input("please enter boot file to boot path:")
        if os.path.exists(filepath):
            os.system(f"call {filepath}")
            break
        else:
            print("File not found")
    