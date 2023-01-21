import socket

sc = socket.socket()
sc.bind(('',555))
sc.listen(5)
sc.accept()
sc.close()
