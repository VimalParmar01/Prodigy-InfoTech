import scapy.all as scapy
import time
import os
import sys
log_file_path = "packet_analyzer_log.txt"
def log_packet(packet):
    with open(log_file_path, "a") as log_file:
        src_ip = packet[scapy.IP].src if scapy.IP in packet else "N/A"
        dst_ip = packet[scapy.IP].dst if scapy.IP in packet else "N/A"
        protocol = packet.proto if scapy.IP in packet else "N/A"
        payload = str(packet.payload) if packet.payload else "No Payload"

        log_file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log_file.write(f"Source IP: {src_ip}\n")
        log_file.write(f"Destination IP: {dst_ip}\n")
        log_file.write(f"Protocol: {protocol}\n")
        log_file.write(f"Payload: {payload}\n")
        log_file.write("-" * 50 + "\n")

def packet_callback(packet):
    print(f"Packet captured: {packet.summary()}")
    log_packet(packet)

def main():
    print("---------------- Network Packet Analyzer ----------------")
    print("This tool captures and analyzes network packets.")
    print("It displays information such as source and destination IP addresses, protocols, and payload data.")
    print("Ensure you have explicit permission to use this tool on any network or system.")
    
    accept_terms = input("\nDo you accept these terms and conditions? (Yes/No): ")
    if accept_terms.strip().lower() != 'yes':
        print("You must accept the terms and conditions before using this program.")
        sys.exit()

    print("Starting packet capture... Press Ctrl+C to stop.")
    try:
        scapy.sniff(prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"\nThe log file has been saved to: {os.path.abspath(log_file_path)}")

if __name__ == "__main__":
    main()
