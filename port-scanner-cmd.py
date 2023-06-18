import os
import socket
import threading
import time
from colorama import Fore, Style, init

init()  # Initialize colorama

def clear_screen():
    # Clear the command prompt window
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux and macOS
        os.system("clear")

def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second

        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))

        # Check if the connection was successful
        if result == 0:
            print(f"{Fore.GREEN}Port {port} is open{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Port {port} is closed{Style.RESET_ALL}")

        # Close the socket
        sock.close()
    except socket.error:
        print(f"{Fore.RED}Could not connect to {host}:{port}{Style.RESET_ALL}")

def port_scan(host, start_port, end_port):
    print(f"Scanning ports on {host}...\n")
    for port in range(start_port, end_port + 1):
        # Create a new thread for each port scan
        thread = threading.Thread(target=scan_port, args=(host, port))
        thread.start()
        time.sleep(0.1)  # Add a slight delay for the animation effect

# Get user input
host = input("Enter the IP address to scan: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Clear the screen before running the script
clear_screen()

# Usage example
port_scan(host, start_port, end_port)


#########################################
#                                       #
#   Please join my discord community:   #
#    https://discord.gg/QKJPfpaFUk      #
#                                       #
#########################################