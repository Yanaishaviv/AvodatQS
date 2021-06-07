import scapy.all as scapy
import constants

def check(packet):
    if (scapy.IP in packet):
        return packet[scapy.IP].dst == constants.SERVER_IP and packet[scapy.IP].src == constants.CLIENT_IP  
    return False



# packets = scapy.all.sniff(2)
packets = 3
yes = scapy.sniff(count = constants.NUMBER_OF_PACKETS, lfilter = check)
print('success ', yes[2][scapy.RAW].load)
