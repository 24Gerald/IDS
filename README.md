# Intrusion Detection System (IDS)

## Overview
This project is an **Intrusion Detection System (IDS)** that monitors network traffic for suspicious activity, logs potential attacks, and provides a web dashboard for real-time monitoring.

## Features
- **Packet Sniffing**: Monitors network traffic using Python (`scapy`).
- **SQL Logging**: Stores detected intrusions in MySQL/PostgreSQL.
- **Threat Intelligence**: Checks attacker IPs against known blacklists.
- **Web Dashboard**: Uses Flask & JavaScript for real-time visualization.
- **Automation & Alerts**: Sends notifications and blocks malicious IPs.

## Technologies Used
- **Backend**: Python (Flask, Scapy, MySQL Connector)
- **Frontend**: HTML5, JavaScript (Chart.js, Fetch API)
- **Database**: MySQL/PostgreSQL
- **Scripting**: Bash for automation

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/ids-system.git
cd ids-system
```

### 2. Install Dependencies
#### Python Requirements
```sh
pip install flask scapy mysql-connector-python requests
```

#### Database Setup (MySQL Example)
```sh
CREATE DATABASE ids_db;
USE ids_db;
CREATE TABLE intrusions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255),
    port INT,
    payload TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Run the Packet Sniffer
```sh
python sniffer.py
```

### 4. Start the Web Dashboard
```sh
python app.py
```

### 5. View Dashboard
Open your browser and go to:
```
http://localhost:5000
```

## Sample Code
### Packet Sniffer (Python)
```python
from scapy.all import sniff, IP, TCP
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="password", database="ids_db")
cursor = conn.cursor()

def log_attack(ip, port, payload):
    cursor.execute("INSERT INTO intrusions (ip, port, payload) VALUES (%s, %s, %s)", (ip, port, payload))
    conn.commit()

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip = packet[IP].src
        port = packet[TCP].dport
        payload = bytes(packet[TCP].payload).hex()
        
        print(f"[*] Suspicious Packet: {ip}:{port} - {payload}")
        log_attack(ip, port, payload)

sniff(prn=packet_callback, store=False)
```

## Future Enhancements
- AI-based anomaly detection
- SIEM integration (Splunk, ELK Stack)
- GeoIP tracking

## License
This project is open-source under the MIT License.

## Author
**24Gerald** - [GitHub Profile](https://github.com/24Gerald)
