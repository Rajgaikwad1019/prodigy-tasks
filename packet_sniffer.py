from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"
        else:
            protocol_name = "Other"

        
        print(f"Source: {ip_src} -> Destination: {ip_dst} | Protocol: {protocol_name}")
        
        
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload if packet.haslayer(TCP) else packet[UDP].payload)
            if len(payload) > 0:
                print(f"   Payload: {payload[:50]}...")

def main():
    print("--- Network Packet Analyzer ---")
    print("Capturing packets... (Press Ctrl+C to stop early)")
    
    
    sniff(prn=packet_callback, count=20)

if __name__ == "__main__":

    main()
