from scapy.all import *
from scapy.layers.http import HTTPRequest
"""
def process_packet(packet):
    '''
    This function is executed whenever a packet is sniffed
    '''
    if packet.haslayer(HTTPRequest):
        # if this packet is an HTTP Request
        # get the requested URL
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        # get the requester's IP Address
        ip = packet[IP].src
        # get the request method
        method = packet[HTTPRequest].Method.decode()
        print(f"\n[+] {ip} Requested {url} with {method}")
        if show_raw and packet.haslayer(Raw) and method == "POST":
            # if show_raw flag is enabled, has raw data, and the requested method is "POST"
            # then show raw
            print(f"\n[*] Some useful Raw data: {packet[Raw].load}")

This is mostly to draw inspiration from, not actually in use yet
"""
packets=sniff(filter="host 100.64.1.107 and not arp", prn=lambda x:x.show())
print(packets)
