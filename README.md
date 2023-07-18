# UTokyo-Cyber-Security-Project

# DISCLAIMER
This is a proof of concept project. Do NOT use on networks you don't have authorization to monitor.




## General notes for the project (setup etc.)

Connected to the RPi via SSH and PuTTY

Enabled Ipv4 forwarding by uncommenting

`net.ipv4.ip_forward = 1`

in /etc/sysctl.conf

This is essential if one wishes to forward the packets. The RPi can also act as a block for any outdoing traffic (or incoming for that matter) if this settings is set to  0. This means that ARP-spoofing with this setting set to 0 essentially is a Denial of Service attack on the IoT device in question (here Arduino).

installed tshark with 

`sudo apt install tshark`


basic filter for target IP address without the spam ARP messages from the spoofing:

`sudo tshark -f "host [target IP] and not arp"`

or in /Packet_Cap/sniff.py:

`packets = sniff(filter="host [target IP] and not arp", prn=lambda x:x.summary())` 


download scapy with 

`sudo apt get scapy`

Note: `pip install scapy` didnt work, probably a PATH problem that I don't want to deal with


## What works so far:
1) main.py to spoof ARP packets on the network and get an Arduino that is constantly pinging google.com to send its packets to the RPi instead of the default gateway of the network
2) able to see the sent packets via tshark in another console window.
3) able to remotely acces the RPi using the `ssh -R 2222:localhost:22 magnu@[RPi-IP address]`

## What's left to do
1) COMPLETED! Find a way to remotely control the RPi from a different network (an idea could be to make it send data to - and receive instructions from a website)
2) Alter the sniffed data in some meaningful way
3) OS fingerprinting for to identify potential targets. Use p0f or nmap for this


## What a potential attack could look like

1) The attacker looks up what devices are on the network with the command `arp -a` to determine the MAC addresses
2) The MAC address can be used to identify the vendor on websites such as [OUI Lookup](https://ouilookup.com/search/B827EB127F51)

   Alternatively tools like [Advanced IP Scanner](https://www.advanced-ip-scanner.com/) can be used.
3) Once the attacker has identified an attackable IoT device, the RPi can be directed at the target's IP address and begin ARP-spoofing.
4) The target will now start to send packets to the RPi, which can be read using tshark.
