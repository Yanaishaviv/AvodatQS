import scapy.all as scapy
import constants

def check(packet):
    if (scapy.IP in packet):
        return packet[scapy.IP].src == constants.SERVER_IP  
    return False



# packets = scapy.all.sniff(2)
packets = 3
yes = scapy.sniff(count = 1, lfilter = check)
print('success ',yes[0].show())
