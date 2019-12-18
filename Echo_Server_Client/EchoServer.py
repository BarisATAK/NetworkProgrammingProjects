import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM -> default TCP, AF_INET -> IPV4
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = '127.0.0.1' # LOCALHOST
port = 3000 # Recommended above 1024 because lesser than 1024 are reserved for Standard Internet Protocol.

print("Server running on %s: %d" % (host,port))

# Bind the own address
sock.bind((host, port))
sock.listen()
client, address = sock.accept() # Waits for an incoming connection. Return host and port number.

while True:
    data = client.recv(1024) # Bounded 1024 characters.
    if data:
        print("Received from client: %s" % data.decode('utf-8'))
        client.send(data)
client.close()