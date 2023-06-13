# UTokyo-Cyber-Security-Project

# DISCLAIMER
This is a proof of concept project. Do NOT use on networks you don't have authorization to monitor.




## notes for the project so far

Connected to the RPi via SSH and PuTTY

Enabled Ipv4 forwarding by setting uncommenting

`net.ipv4.ip_forward = 1`

in /etc/sysctl.conf

installed tshark with 

`sudo apt install tshark`

basic filter for target IP address:

`sudo tshark -f "host [target IP]"`

download scapy with 

`sudo apt get scapy`

Note: `pip install scapy` didnt work, probably a PATH problem that I don't want to deal with

## What works so far:
1) main.py to spoof ARP packets on the network and get an Arduino that is constantly pinging google.com to send its packets to the RPi
2) able to see the sent packets via tshark in another console window.
