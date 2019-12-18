from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

Host = ''
Port = 33000
BufSize = 1024
Addr = (Host, Port)
Server = socket(AF_INET, SOCK_STREAM)
Server.bind(Addr)

def AcceptIncomingConnections():
	while True: # Waits for incoming connections.
		client, client_address = Server.accept() # Returns host value and port number.
		print("%s:%s has connected." % client_address)
		addresses[client] = client_address #??????????client nasıl dizi oluyor
		Thread(target = HandleClient, args=(client,)).start() #????????????????????????

def HandleClient(client): # Takes client socket as argument
	name = client.recv(BufSize).decode("utf8")############3
	message = "%s has joined the chat!" %name
	client.send(bytes(message, "utf8"))
	Broadcast(bytes(message, "utf8"))
	clients[client] = name
	while True:
		message = client.recv(BufSize)
		if message != bytes("{quit}", "utf8"):
			Broadcast(message, name + ": ")
		else:
			client.send(bytes("{quit}"), "utf8")
			client.close()
			del clients[client]
			Broadcast(bytes("%s has left the chat." % name, "utf8"))
			break

def Broadcast(message, prefix = ""): # Prefix is for name identification.
	"""Broadcasts a message to all clients."""
	for sock in clients:
		sock.send(bytes(prefix, "utf8") + message)

if __name__ == "__main__":
	Server.listen(5) # Listens for 5 connections at max.
	print("Waiting for connection...")
	AcceptThread = Thread(target = AcceptIncomingConnections)
	AcceptThread.start() # Stars the infinite loop.
	AcceptThread.join()
	Server.close()


