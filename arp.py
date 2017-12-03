import sys
from datetime import datetime

try:

	interface = raw_input("[*] Hangi interface'te tarama yapilsin (ORN: enp5s0): ")
	ips = raw_input("[*] Hangi IP araliginda taratilsin (ORN: 192.168.1.0/24): ")

except KeyboardInterrupt:
	
	print "\n[*] Cikiliyor."
	sys.exit(1)

print "\n[*] Taraniyor..."

start_time = datetime.now()

from scapy.all import srp, Ether, ARP, conf

conf.verb = 0
ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface = interface,inter = 0.1)

print "MAC - IP\n"

text_file = open("arp_liste.txt", "w")

for snd, rcv in ans:
	
	text_file.write(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"))
	text_file.write("\n")
	print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")


text_file.close()

stop_time = datetime.now()
total_time = stop_time - start_time

print "\n[*] Tarama tamamlandi."
print "[*] TXT dosyasi olusturuldu."
print ("[*] Gecen sure: %s" %(total_time))


