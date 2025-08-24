import sys
import socket 

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    
    except socket.gaierror:
        print(f"[-] Error: Hostname '{target}' could not be resolved")
        sys.exit()
        
    except socket.error:
        print(f"[-] Error: Cannot connect to '{target}' server")
        sys.exit()
        
    except KeyboardInterrupt:
        print("\n[!] Exiting program.")
        sys.exit()
        

def main():
    print(r"""
  _____           _           _____                                 
 |  __ \         | |         / ____|                                
 | |__) ___  _ __| |_       | (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ _ \| '__| __|       \___ \ / __/ _` | '_ \| '_ \ / _ | '__|
 | |  | (_) | |  | |_        ____) | (_| (_| | | | | | | |  __| |   
 |_|   \___/ |_|   \__|      |_____/ \___\__,_|_| |_|_| |_|\___|_|   
""")
    print("=" * 70)
    
    print("\n\t\tCreated by 'codwolf' ")

    target_host = input("\n\nEnter the Target IP (or) Hostname: ")
    port_range = input("\n\nEnter the port range (e.g., '1-456'): ")    
    
    print(f"\n[+] Scanning {target_host}...\n") 
    
    try:
        start_port, end_port = sorted(map(int, port_range.split('-')))
        open_ports = []
        
        for port in range(start_port, end_port + 1):
            if scan_port(target_host, port):
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
        
        if not open_ports:
            print("\n[-] No open ports were found in the specified range.")

    except ValueError:
        print("[-] Invalid port range format. Please use 'start-end' (e.g., 1-1024).")
        sys.exit(1)


if __name__ == "__main__":
    main()
