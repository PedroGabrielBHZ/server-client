import socket

IP_ADDRESS = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))
sock.send(MESSAGE)
data = sock.recv(BUFFER_SIZE)
sock.close()

print("received data: <" + data.decode("utf-8") + ">")
