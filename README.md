# 🕵️‍♂️ Port Scanner  

## 🔍 A simple multi-threaded port scanner that checks for open ports on a target IP address!  

![Port Scanner](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExanB2cG03eDhyZGJtdXQ2MTd1MGh3bThmb2Z0OXd3dm5keDU0cWhrZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/i9cngh3Kw09GxlsrFP/giphy.gif)  


---

## 📌 Features  
✅ **Multi-threaded scanning** – Faster results by scanning multiple ports simultaneously!  
✅ **Logging system** – Keeps track of each scan in `log.txt`!  
✅ **Scan counter** – Counts how many times you've used the scanner (`scan_count.txt`)!  
✅ **IPv4 & TCP support** – Scans based on common networking standards!  

---

## 🚀 How It Works  

1️⃣ **Enter the target IP address**  
2️⃣ **The script scans the ports in the list**  
3️⃣ **Open and closed ports are displayed**  
4️⃣ **Results are logged in `log.txt`**  
5️⃣ **Scan count is updated in `scan_count.txt`**  

---

## 🛠️ Installation & Usage  

### 🔧 Requirements  
Make sure you have **Python 3.x** installed!  

### 🏃‍♂️ Run the Scanner  

```bash
git clone https://github.com/yourusername/PortScanner.git
cd PortScanner
python port_scanner.py
```
### ⚡Example Output

```kotlin
Enter the IP address you want to scan: 192.168.1.1
Port 22 is open!
Port 80 is open!
Port 443 is open!
Port 25 is closed!
```
### Results are also saved in log.txt for later reference! 📄


