# DEDSEC-SCAN
## Dedsec Vulnerability Scanner

Dedsec Vulnerability Scanner is a sophisticated tool for detecting vulnerabilities on a network using Nmap and its NSE scripts. It features an interactive menu, animated banner, and is designed for use with Termux on Android devices.

## Features

- Scans for common vulnerabilities using Nmap's `vuln` script.
- Interactive menu for easy navigation with animated text.
- Animated banner with a stylish "A DEDSEC" logo.
- Ability to get the IP address of a domain using `nslookup`.
- Option to update the script directly from the menu.
- Works seamlessly with Termux on Android devices.

## Prerequisites

- Termux installed on your Android device.
- `nmap`, `python`, `dnsutils`, and `colorama` installed via Termux package manager.

## Using

   ```bash
   git clone https://github.com/yourusername/dedsec-vuln-scanner.git
   cd DEDSEC-SCAN
   pip install -r requirements.txt
    chmod +x famous.scan.py
  ./famous.scan.py
