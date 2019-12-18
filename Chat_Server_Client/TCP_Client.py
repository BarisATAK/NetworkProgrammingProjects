import socket

def ClientProgram():
	host = socket.gethostname() # Get the localhost (Same as server).
	port = 3000 # Server's port number

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new socket.
	clientSocket.connect((host,port)) # Connect to the server.

	message = input("->") # Take the message.
	
	while message.lower().strip() != 'bye':
		clientSocket.send(message.encode()) # Send the message.
		data = clientSocket.recv(1024).decode() # Receive response.

		print("Message from server: " + str(data))
		message = input("->") # Take message again.
	clientSocket.close() # Close the connection.

if __name__ == '__main__':
	ClientProgram()