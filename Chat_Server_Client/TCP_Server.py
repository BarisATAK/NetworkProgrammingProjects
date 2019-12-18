import socket

def ServerProgram():
	print("Server started listening...")
	host = socket.gethostname() # Get the host name.
	port = 3000 # Recommended above 1024 because lesser than 1024 are reserved for Standard Internet Protocol.

	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket.
	serverSocket.bind((host,port)) # Bind socket object to a host and port number.

	serverSocket.listen(2) # Server can listen 2 client simultaneously.
	conn, address = serverSocket.accept() # Accepts incoming connections and returns a tuple of (conn, address).
	print(str(address) + " address is connected...")
	while True:
		data = conn.recv(1024).decode() # Receive data stream. It bounded with 1024 bytes.
		if not data:
			break # If data is not received, break.
		print("Message from connected user: " + str(data))
		data = (input("->"))
		conn.send(data.encode()) # Send data to the client.
	conn.close() # Close the connection.

if __name__ == '__main__':
	ServerProgram()