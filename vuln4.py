from scapy.all import *
source_IP = "127.0.0.1"
target_IP = "127.0.0.1"
source_port = 65000
i = 1

while True:
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 23456)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print ("packet sent ", i)
   i = i + 1