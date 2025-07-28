from scapy.all import sniff

# Function to process each packet
def analyze_packet(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"[+] Packet: {ip_layer.src} --> {ip_layer.dst} | Protocol: {ip_layer.proto}")

# Start packet sniffing
print("Starting packet sniffing... Press Ctrl+C to stop.")
sniff(prn=analyze_packet, store=False)
