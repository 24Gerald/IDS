from scapy.all import sniff, IP, TCP
import mysql.connector

# Connect to Database
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
        
        print(f"Suspicious Packet: {ip}:{port} - {payload}")
        log_attack(ip, port, payload)

sniff(prn=packet_callback, store=False)
