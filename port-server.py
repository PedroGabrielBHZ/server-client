import socket

IP_ADDRESS = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT))
sock.listen(1)

conn, address = sock.accept()
print("Connection from: " + address[0] + " Port: " + str(address[1]))

while True:
    data = conn.recv(BUFFER_SIZE).decode("utf-8")
    if not data:
        break
    print("received data: " + data)
    conn.send(str.encode("Echo: " + data))
conn.close()
