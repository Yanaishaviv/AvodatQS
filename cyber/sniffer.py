import constants
import pyshark as ps
import functions
import RSA
import shor_try
import AES

# create sniffer object
cap = ps.LiveCapture(display_filter='tcp and ip.src == 10.0.0.4 or ip.dst == 10.0.0.4')
# prepare the list to hold the public key
public_key = [] 
# count how many packets with data reached the computer  
count = 0 
for i in cap.sniff_continuously(packet_count = 20):
    if 'payload' in dir(i.tcp):
        if count < 2: 
            # the first two are sent from the server and contain the public key 
            public_key.append(functions.parse_sniff_int(i.tcp.payload))
            count += 1
            print(i.tcp.payload)
            print(count, 'count')
        if count>=2: 
            # the third is sent from the client and contains the AES key, encrypted
            if (i.ip.dst == constants.SERVER_IP): 
                aes_key = (i.tcp.payload.binary_value.decode())
                break

p = 1 
while p==1: 
    # if the shor function fails, it return p=1. so try again until it works
    (p, q) = shor_try.shor(public_key[1])

# calculate the totient to prepare d    
phi = (p-1)*(q-1) 

# find d with phi and e
d = RSA.multiplicative_inverse(public_key[0], phi) 

# save the private key
private_key = (d, public_key[1])

# formatting the AES key in a readable form
lst_aes_key = functions.parse_string_data(aes_key) 

# decrypt the cipher and find the aes key
final_key = RSA.decrypt(private_key, lst_aes_key) 

# create an AES object
aes_obj = AES.AES(final_key) 

# sniff 10 messages
for i in cap.sniff_continuously(packet_count=10):
    if 'payload' in dir(i.tcp): # only print messages with data
        coded_msg = i.tcp.payload.binary_value 
        # message in bin
        encr_msg = coded_msg.decode()
        # encrypted message 
        msg = aes_obj.decrypt(encr_msg)
        # readable message
        if (i.ip.dst == constants.SERVER_IP):
            sender = 'client:'
        else:
            sender = 'server:'
        print(sender, msg)

