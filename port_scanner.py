import socket
import threading
import os

# Get current directory to make files in the same directory as project.
current_dir = os.path.dirname(__file__)

scan_count_file = os.path.join(current_dir, 'scan_count.txt')
log_file = os.path.join(current_dir, 'log.txt')

# Constant variable that contains the port numbers that will be scanned.
PORTS = [20, 21, 22, 25, 53, 80, 110, 139, 443, 445, 890, 1337, 1433, 3389, 5555, 65535, 8000, 8008, 8443, 8888, 9000, 9009]

# Keeps count of scans & outputs to a file 'scan_count.txt'.
def count_scans():
    
    try:
        with open(scan_count_file, 'r') as count_file:
            count = count_file.readline()
            count_file.close()
            
        int_count = int(count) + 1
        with open(scan_count_file, 'w') as count_file:
            count_file.write(str(int_count))
            count_file.close()
        return str(int_count)
    
    except FileNotFoundError:
        with open(scan_count_file, 'w') as count_file:
            count_file.write('1')
            count_file.close()
            return '1'

# Writes scan results to file 'log.txt'.
def write_logs(scan_count, ip_addr, log_results):
    
    with open(log_file, 'a') as my_logs:
        my_logs.write("Number of Scans: " + scan_count + '\n')
        my_logs.write(f"IP Address Scanned: {ip_addr}\n")
        for result in log_results:
            my_logs.write(result + '\n')
            # Fun separation between results in log.txt.
        my_logs.write('--------------------\n')
        my_logs.close()

def scan_port(ip, port, log_results):
        
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
            
        log_results.append(result_txt)

# Allows multiple ports to be scanned concurrently.
def thread_scans(ip_addr, log_results):
    
    threads = []
    for port in PORTS:
        t = threading.Thread(target=scan_port, args=(ip_addr, port, log_results))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
def run_program():
    
    running = True
    
    while running:
        
        # Create logging results list to iterate through and write to the log.txt file.
        logging_results = []
        
        ip = input("Enter the IP address you want to scan: ")
        
        thread_scans(ip, logging_results)
        scan_counter = count_scans()
        write_logs(scan_counter, ip, logging_results)
        
        print('')
        run_again = input("Would you like to scan another ip address? Y for yes and N for no: ")
        print('')
        
        if run_again != 'y':
            print("Thank you for using my port scanner! Check out my GitHub for more projects in the future.")
            running = False
        

if __name__ == "__main__":
    run_program()
