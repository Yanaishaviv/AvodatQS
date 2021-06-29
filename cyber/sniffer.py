import constants
import pyshark as ps
import functions
import RSA
import shor_try
import AES

cap = ps.LiveCapture(display_filter='tcp and ip.src == 10.0.0.4 or ip.dst == 10.0.0.4')
public_key = []
count = 0
for i in cap.sniff_continuously(packet_count = 20):
    if 'payload' in dir(i.tcp):
        if count < 2:
            public_key.append(functions.parse_sniff_int(i.tcp.payload))
            count += 1
            print(i.tcp.payload)
            print(count, 'count')
        if count>=2:
            if (i.ip.dst == constants.SERVER_IP):
                aes_key = (i.tcp.payload.binary_value.decode())
                print(aes_key, 'line 16')
                break

p = 1
while p==1:
    (p, q) = shor_try.shor(public_key[1])
    
phi = (p-1)*(q-1)

d = RSA.multiplicative_inverse(public_key[0], phi)

private_key = (d, public_key[1])

lst_aes_key = functions.parse_string_data(aes_key)
final_key = RSA.decrypt(private_key, lst_aes_key)

aes_obj = AES.AES(final_key)
# for i in general_cap.sniff_continuously(packet_count = 2):
#     if 'payload' in dir(i.tcp):
#         aes_key = (i.tcp.payload.binary_value.decode())
#         print(aes_key, 'line 29')




for i in cap.sniff_continuously(packet_count=10):
    if 'payload' in dir(i.tcp):
        coded_msg = i.tcp.payload.binary_value
        encr_msg = coded_msg.decode()
        msg = aes_obj.decrypt(encr_msg)
        if (i.ip.dst == constants.SERVER_IP):
            sender = 'client:'
        else:
            sender = 'server:'
        print(sender, msg)

