**# Network Scanner 🔍🌐**



A professional Python-based Network Scanner developed for cybersecurity reconnaissance.  

This tool identifies live hosts on a local network by sending ARP requests and capturing responses to map IP addresses with their corresponding MAC addresses.



---



\## 📌 Project Overview



The Network Scanner is a command-line utility designed to perform \*\*Layer 2 network scanning\*\*.  

It helps in discovering active devices within a given IP address or subnet range, which is a fundamental task in cybersecurity assessments and network enumeration.



---



\## 🚀 Key Features



\- Scan a single IP address or an entire subnet

\- Discover live hosts on the local network

\- Display IP address and MAC address of detected devices

\- Fast and lightweight ARP-based scanning

\- Command-line interface for flexibility

\- Compatible with Windows (Npcap required)



---



\## 🛠️ Technologies \& Tools



\- \*\*Python 3\*\*

\- \*\*Scapy\*\*

\- \*\*Networking Protocols:\*\* ARP, IP, MAC

\- \*\*Command Line Interface (CLI)\*\*



---



\## 📂 Project Structure





---



\## ⚙️ Installation \& Setup



\### 1️⃣ Clone the Repository

```bash

git clone https://github.com/your-username/network-scanner.git

cd network-scanner



2️⃣ Install Required Python Library

pip install scapy





3️⃣ Windows Requirement (Important)



For Windows systems, install Npcap to enable Layer 2 packet access:



Download from: https://npcap.com/



During installation, enable:



✔ WinPcap API-compatible mode



✔ Install for all users



▶️ Usage



Run the script as Administrator:



python network\_scanner.py -t 192.168.1.1/24



Alternative command:

python network\_scanner.py --target 192.168.1.1/24







📊 Sample Output

IP Address            MAC Address

-------------------------------------------

192.168.1.1           00:14:22:01:23:45

192.168.1.10          08:00:27:ab:cd:ef





⚠️ Disclaimer



This project is created strictly for educational purposes.

Only scan networks that you own or have explicit permission to test.





👤 Author



Utsav Dineshbhai Chopda

Cybersecurity Enthusiast

📍 Pune, Maharashtra, India

