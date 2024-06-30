#!/data/data/com.termux/files/usr/bin/python

import subprocess
import sys
import os
import time
from colorama import Fore, Style

def print_banner():
    banner = """
    ███████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ 
    ██╔════╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
    ███████╗███████║█████╗  ██████╔╝█████╗  ██████╔╝
    ╚════██║██╔══██║██╔══╝  ██╔══██╗██╔══╝  ██╔══██╗
    ███████║██║  ██║███████╗██║  ██║███████╗██║  ██║
    ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                product by  DEDSEC
    """
    for char in banner:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(0.005)
    print(Style.RESET_ALL)

def run_nmap_scan(ip_address):
    try:
        print(f"Scanning for vulnerabilities on {ip_address}...")
        result = subprocess.run(
            ['nmap', '-Pn', '--script', 'vuln', ip_address],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def get_ip_address(domain):
    try:
        result = subprocess.run(
            ['nslookup', domain],
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout
        ip_address = output.split()[-1]
        print(f"The IP address of {domain} is {ip_address}")
        return ip_address
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def update_script():
    print("Updating the script...")
    subprocess.run(['git', 'pull'])
    print("Update complete.")

def print_menu():
    menu = """
    1. Scan for Vulnerabilities
    2. Get IP Address of a Domain
    3. Update the Script
    4. Exit
    """
    for char in menu:
        print(Fore.GREEN + char, end='', flush=True)
        time.sleep(0.005)
    print(Style.RESET_ALL)

def main_menu():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            ip_address = input("Enter the IP address to scan: ")
            run_nmap_scan(ip_address)
        elif choice == '2':
            domain = input("Enter the domain to get IP address: ")
            ip_address = get_ip_address(domain)
            if ip_address:
                run_nmap_scan(ip_address)
        elif choice == '3':
            update_script()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print_banner()
    main_menu()
