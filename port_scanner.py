# PortScanner
# │── README.md
# │── port_scanner.py
# │── scan_count.txt  (automatically created)
# │── log.txt  (automatically created)

import socket
import threading

logging_results = []
ports = [20, 21, 22, 25, 53, 80, 110, 139, 443, 445, 890, 1337, 1433, 3389, 5555, 65535, 8000, 8008, 8443, 8888, 9000, 9009]
ip = input("Enter the IP address you want to scan: ")

def count_scans():
    # Keeps count of scans & outputs to a file 'scan_count.txt'.
    try:
        with open('scan_count.txt', 'r') as count_file:
            count = count_file.readline()
            count_file.close()
            
        int_count = int(count) + 1
        with open('scan_count.txt', 'w') as count_file:
            count_file.write(str(int_count))
            count_file.close()
        return str(int_count)
    
    except FileNotFoundError:
        with open('scan_count.txt', 'w') as count_file:
            count_file.write('1')
            count_file.close()
            return '1'

def write_logs(scan_count):
    # Writes scan results to file 'log.txt'.
    with open('log.txt', 'a') as my_logs:
        my_logs.write("Number of Scans: " + scan_count + '\n')
        for result in logging_results:
            my_logs.write(result + '\n')
            
        my_logs.write('--------------------\n')
        my_logs.close()

def scan_port(ip, port):
        global logging_results
        
        try:
            # Sets the socket to connect to IPv4 addresses and TCP streams.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                result_txt = f"Port {str(port)} is open!"
                print(result_txt)
            else:
                result_txt = f"Port {str(port)} is closed!"
                print(result_txt)
            s.close()
        except socket.error:
            print("Couldn't connect to the target.")
            
        logging_results.append(result_txt)


def thread_scans():
    # Allows multiple ports to be scanned concurrently.
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
# Calls the functions to run the whole program.
if __name__ == "__main__":
    thread_scans()
    scan_counter = count_scans()
    write_logs(scan_counter)
