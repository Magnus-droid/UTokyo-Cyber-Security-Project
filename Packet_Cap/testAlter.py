from scapy.all import *
import sys
from time import sleep
import requests

payload = "<script>alert('Hello World');</script>"
payload2 = "Hello World"

def change_packets(source, destination, dport):
	query = IP(src=source, dst=destination)/UDP(dport=int(dport))/payload2
	send(query)

while 1:
	change_packets(sys.argv[1], sys.argv[2], sys.argv[3])
	#r=requests.get(url="http://100.64.1.22/H")
	#sleep(2)
	#t=requests.get(url="http://100.64.1.22/L")
	sleep(2)

