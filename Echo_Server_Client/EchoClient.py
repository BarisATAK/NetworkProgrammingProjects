import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM -> default TCP, AF_INET -> IPV4
host = '127.0.0.1' # LOCALHOST
port = 3000 # Recommended above 1024 because lesser than 1024 are reserved for Standard Internet Protocol.

print("Connecting to %s port %s " % (host, port))

try:
    sock.connect((host, port))
    message = input("Client -> ")
    while message != 'exit':
        sock.sendall(message.encode('utf-8'))
        data = sock.recv(1024)
        print('Received: %s ' % data.decode('utf-8'))
        message = input('Client -> ')
except socket.gaierror as e:
    print("Socket error: %s" % str(e))
except Exception as e:
    print(e)
finally:
    sock.close()
