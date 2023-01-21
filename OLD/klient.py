import socket

ip = input("Podaj ip ZIOM: ")
port = int(input("Podaj port ZIOMSON: "))

sc = socket.socket()
sc.connect((ip,port))
sc.close()
