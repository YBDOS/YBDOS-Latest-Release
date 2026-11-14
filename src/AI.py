import os
import sys
import time
import random
import threading
import requests
key=""
URL=""
Modelname=""
def ai_com():
    print("starting AI.COM")
    import time
    import random
    time.sleep(random.randint(1,3))
    a=input("Start AI must Include some lib,Continue[Y/N]?")
    if a.upper()=="Y":
        print("Including requests lib...")
        import requests
        time.sleep(random.randint(1,3))
        print("Including os lib...")
        import os
        time.sleep(random.randint(1,3))
        print("Including sys lib...")
        import sys
        time.sleep(random.randint(1,3))
        print("Including threading lib...")
        import threading
        time.sleep(random.randint(1,3))
        print("Including platform lib...")
        import platform
        time.sleep(random.randint(1,3))
        print("Including socket lib...")
        import socket
        time.sleep(random.randint(1,3))
        print("Including getpass lib...")
        import getpass
        time.sleep(random.randint(1,3))
        print(r"run goto AIcommand")
        edit_AI()
    elif a.upper()=="N":
        print("Include Fail,return to DOS.")
        return
    else:
        print("Invalid input. Please enter a valid value.")
        time.sleep(1)
        print("Uknown Error,Will Restart program.")
        time.sleep(random.randint(1,3))
        print("\033c")
        time.sleep(random.randint(1,3))
        ai_com()
def edit_AI():
    global key,URL,Modelname
    while True:
        command_AI=input(r"CommandforAI\>")
        if command_AI.startswith("set "):
            try:
                lst=command_AI.split()
                if "URL=" in lst[1]:
                    URL=(lst[1])[4:]
                elif "key=" in lst[1]:
                    key=(lst[1])[4:]
                elif "Modelname=" in lst[1]:
                    Modelname=(lst[1])[10:]
                else:
                    print("Unknown variable")
            except:
                print("Run Error,Will Restart program.")
                print("\033c")
                ai_com()
        elif command_AI=="restart program":
            ai_com()
        elif command_AI=="run AI":
            run_ai()
        elif command_AI=="exit" or command_AI=="quit":
            break
def run_ai():
    global key, URL, Modelname
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }

    print("\nModem dialing... OK. Connected.")
    print("Press Ctrl+C to disconnect.\n")

    while True:
        try:
            user_input = input("EXPERT> ").strip()
            
            if not user_input:
                continue
            
            stop_spinner = threading.Event()
            def spin():
                chars = ['-', '\\', '|', '/']
                i = 0
                while not stop_spinner.is_set():
                    sys.stdout.write(f"\rProcessing... {chars[i % 4]}")
                    sys.stdout.flush()
                    i += 1
                    time.sleep(1.0)
                    
            spinner_thread = threading.Thread(target=spin)
            spinner_thread.start()
            
            data = {
                "model": Modelname, # 🚨 严格对齐
                "messages": [{"role": "user", "content": user_input}]
            }
            
            try:
                response = requests.post(URL, headers=headers, json=data, timeout=30)
                response.raise_for_status()
                ai_reply = response.json()["choices"][0]["message"]["content"]
                
                stop_spinner.set()
                spinner_thread.join()
                sys.stdout.write("\r" + " " * 40 + "\r")
                sys.stdout.flush()
                
                print(f"AI: {ai_reply}\n")
                
            except Exception as e:
                stop_spinner.set()
                spinner_thread.join()
                sys.stdout.write("\r" + " " * 40 + "\r")
                sys.stdout.flush()
                # 打印具体的错误原因，方便排错
                print(f"Run Error. Detail: {e}")
                return
        except KeyboardInterrupt:
            return
ai_com()

