# 🔍 Python Port Scanner

A simple **TCP port scanner** written in Python using the `socket` library. This tool checks for open ports on a target host within a given port range.

---

## 🚀 Features
- Scan a target by **IP address** or **hostname**
- Specify a **custom port range**
- Lists all **open TCP ports**
- Handles common errors (invalid host, connection issues, invalid port range)
- Lightweight, no external dependencies

---

## 📦 Installation

Clone the repository:
```bash
git clone [https://github.com/codraja06/port_scanner.git](https://github.com/codraja06/port_scanner.git)
cd port_scanner
```
(Optional) Make the script executable:
```bash
chmod +x port_scanner.py
```

---

## 🛠️ Usage
Run the script:
```bash
python3 port_scanner.py
```
Example:
```
  _____           _           _____                                 
 |  __ \         | |         / ____|                                
 | |__) ___  _ __| |_       | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ _ \| '__| __|       \___ \ / __/ _` | '_ \| '_ \ / _ | '__|
 | |  | (_) | |  | |_        ____) | (_| (_| | | | | | | |  __| |   
 |_|   \___/ |_|   \__|      |_____/ \___\__,_|_| |_|_| |_|\___|_|   

======================================================================

                Created by 'codwolf

Enter the Target IP (or) Hostname: google.com

Enter the port range (e.g., '1-456'): 20-100

[+] Scanning scanme.nmap.org...

[+] Port 80 is OPEN
```

---

## 📂 Project Structure
```
Port-Scanner/
│── port_scanner.py     # Main script
│── README.md           # Documentation
│── requirements.txt    # Dependencies (none required)
│── .gitignore          # Ignored files
