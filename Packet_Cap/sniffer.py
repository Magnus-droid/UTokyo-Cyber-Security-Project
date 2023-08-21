from scapy.all import *
import sys
import datetime
"""
def process_packet(packet):
    '''
    his function is executed whenever a packet is sniffed
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
def readPackets(target):
	filter = "host {} and not arp".format(target)
	packets = sniff(filter=filter, prn=lambda x:x.show())
	print("\tPacket sniffing interrupted. APR spoofing might still be running.")
	wrpcap(str(datetime.datetime.now())+'.pcap', packets)

