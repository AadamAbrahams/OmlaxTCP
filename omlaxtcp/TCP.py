import socket
import time

global s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client(message):
	s.connect(('10.0.0.14', 1234))
	print(message)
	s.send(message.encode())
        s.close

def server_setup():
	s.bind(('', 1234))
	count = 0
	s.listen(5)

def server_recieve():
        c, addr = s.accept()
	data = c.recv(512).decode()
	c.close()
	return data
