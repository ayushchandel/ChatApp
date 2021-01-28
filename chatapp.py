import socket
import os
import threading

myip = input("Enter your IP ")
myport = 1234
oip = input("Enter Other IP ")
oport = 1235
myp = socket.SOCK_DGRAM
afm = socket.AF_INET
s = socket.socket(myp,afm)
s.bind((myip,myport))
print("--------------WELCOME TO CHAT APP-----------------------------")

def sendd():
        while True:
                tosend = input().encode()
                s.sendto(tosend,(oip,oport))
                

def receive():
        while True:
                x = s.recvfrom(1024)
                print(x[0].decode())

x1 = threading.Thread(target=sendd)
x2 = threading.Thread(target=receive)
x1.start()
x2.start()