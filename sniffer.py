from scapy.all import sniff, IP

def process_packet(packet):
    if packet.haslayer(IP):
        ip = packet[IP]
        print("\n Packet Captured")
        print("Source IP:", ip.src)
        print("Destination IP:", ip.dst)
        print("Protocol:", ip.proto)
        print("--------------------------------")

print("Starting Network Sniffer... Press CTRL+C to stop")
sniff(prn=process_packet, store=False)