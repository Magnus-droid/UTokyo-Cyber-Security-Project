# UTokyo-Cyber-Security-Project

# DISCLAIMER
This is a proof of concept project. Do NOT use on networks you don't have authorization to monitor.


## notes for the project so fat

installed tshark with 
`sudo apt install tshark`

basic filter for target IP address:

`sudo tshark -f "host [target IP]"`

download scapy with 
`sudo apt get scapy`

Note: `pip install scapy` didnt work, probably a PATH problem that I don't want to deal with
