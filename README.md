# py-rat

**py-rat** is a minimal Python TCP reverse-shell project built for learning socket programming, client-server communication, and fundamental remote-administration concepts in an isolated, authorized lab.

## Overview

The project has two components:

- `server.py` — runs on a Linux machine and accepts an incoming TCP connection
- `client-rat.py` — runs on an authorized Windows test machine and connects back to the server

Once connected, the Linux operator can send commands, which the Windows client executes and returns as output.

```text
Windows client  ──TCP connect──▶  Linux server :4444
       ▲                                  │
       └──────── command / output ────────┘
```

## Features

- Python-only TCP communication
- Reverse-connection model: the Windows client connects back to the Linux server
- Interactive command prompt on the server
- Newline-delimited UTF-8 messages
- Simple `exit` / `quit` command to close the session
- Suitable for isolated virtual-machine security labs

## Learning Goals

This project can help you understand:

- TCP sockets using Python’s `socket` module
- The difference between bind shells and reverse shells
- Client-server request/response flow
- Text encoding and decoding over a network
- Basic network troubleshooting
- Why authentication, encryption, and access control matter in real remote-administration tools

## Requirements

- Python 3.8 or newer
- Linux host or VM for `server.py`
- Windows VM or authorized Windows test machine for `client-rat.py`
- An isolated lab network, such as VirtualBox/Vmware host-only networking

## Installation

Clone the repository:

```bash
git clone [https://github.com/](https://github.com/)<your-username>/py-rat.git
cd py-rat
```

No external Python packages are required.

## Usage

### 1. Start the Linux server

```bash
python3 server.py
```

Expected output:

```text
[*] Listening on port 4444
[*] Waiting for Windows target to connect...
```

### 2. Start the Windows client

On the authorized Windows test machine, run:

```powershell
python client-rat.py
```

The client should connect back to the Linux server’s IP address on port `4444`.

### 3. Send commands

After the connection is established, type commands at the server prompt:

```text
SHELL> whoami
SHELL> ipconfig
SHELL> dir
SHELL> exit
```

Use `exit` or `quit` to end the current session.

## Project Structure

```text
py-rat/
├── server.py         # Linux-side TCP control server
├── client-rat.py     # Windows-side client
└── README.md
```

## Configuration

By default, the server listens on:

```python
("0.0.0.0", 4444)
```

For a safer local test, bind only to loopback:

```python
server.bind(("127.0.0.1", 4444))
```

If testing between a Linux host and a Windows VM, use an isolated host-only or internal virtual network rather than a public or shared network.

## Security Notes

`py-rat` intentionally lacks production-grade protections. It has:

- No authentication
- No TLS encryption
- No command allowlisting
- No sandboxing
- No audit logging
- No protection against misuse

Treat it as a lab exercise, not as a secure remote-administration tool.

## Known Limitations

- Supports one connected client at a time
- Uses blocking `input()` and `recv()` calls
- Large command output may be split across multiple TCP reads
- Does not implement message-length framing
- No reconnect, timeout, or session-management features

## Roadmap

Possible educational improvements:

- Add command-line arguments for host and port
- Add connection timeouts
- Implement length-prefixed message framing
- Handle multiple clients with threads or `selectors`
- Add optional TLS using Python’s `ssl` module
- Add structured logging
- Add unit tests for encoding, framing, and connection handling

## Responsible Use

Only deploy this project in an environment where you have full authorization, such as:

- Your own computer
- A personal virtual machine lab
- A CTF environment that explicitly permits it
- A security course or lab with written permission

Do **not** use it on public networks, shared Wi-Fi, school or workplace systems, or any machine you do not own.

## License

This project is released under the [MIT License](LICENSE).

## Author

Built by **LooninS** for learning networking, operating systems, and security fundamentals.
