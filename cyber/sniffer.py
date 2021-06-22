import constants
import pyshark as ps

cap = ps.LiveCapture(display_filter='ip.src==10.0.0.4 and tcp')
cap.sniff(timeout=15)

for i in range(len(cap._packets)):
    print(i)
    print(cap._packets[i])

print(len(cap._packets))