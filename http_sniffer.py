# This code is based on an example from The Python Code
# Source URL: https://thepythoncode.com/article/sniff-http-packets-scapy-python
from scapy.all import *
from scapy.layers.http import HTTPRequest
from colorama import init, Fore

init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

def process_packet(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        ip = packet[IP].src
        method = packet[HTTPRequest].Method.decode()
        print(f"{GREEN}[+] {ip} Requested {url} with {method}{RESET}")
        if show_raw and packet.haslayer(Raw) and method == "POST":
            print(f"{RED}[*] Some useful Raw data: {packet[Raw].load.decode()}{RESET}")

def sniff_dat(iface=None):
    if iface:
        sniff(filter="port 80", prn=process_packet, iface=iface, store=False)
    else:
        sniff(filter="port 80", prn=process_packet, store=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HTTP Packet sniffer")
    parser.add_argument("-i", "--iface")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true")
    args = parser.parse_args()
    iface = args.iface
    show_raw = args.show_raw
    sniff_dat(iface)

 
