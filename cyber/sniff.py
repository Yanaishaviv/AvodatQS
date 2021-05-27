import scapy.all as scapy

def check(packet):
    if (scapy.IP in packet):
        return packet[scapy.IP].dst != '192.168.68.108' 
    return False



# packets = scapy.all.sniff(2)
packets = 3
yes = scapy.sniff(count = 10, lfilter = check)
print('success ', yes[0].show())