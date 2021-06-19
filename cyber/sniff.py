import scapy.all as scapy
import constants

def check(packet):
    if (scapy.IP in packet):
        return packet[scapy.IP].dst == '10.0.0.11' or packet[scapy.IP].src == '10.0.0.11'  
    return False



# packets = scapy.all.sniff(2)
packets = 3
yes = scapy.sniff(count = 1, lfilter = check)
print('success ',yes[0].show())
