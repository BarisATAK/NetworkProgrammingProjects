from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from tkinter import*
from PIL import ImageTk, Image
from PIL import ImageTk as itk

def Receive():
	while True:
		try:
			message = clientSocket.recv(BufSize).decode("utf8")
			messageList.insert(END, message)
		except OSError: # Possibly client has left the chat.
			break

def Send(event = None): # event as an argument because it is implicitly passed by Tkinter when the send button on the GUI is pressed.
	message = name.get()
	name.set("")
	clientSocket.send(bytes(message, "utf8"))
	message = myMessage.get() # myMessage is the input field on the GUI.
	myMessage.set("") # Clears input field.
	clientSocket.send(bytes(message, "utf8"))
	if message == "{quit}":
		clientSocket.close()
		root.quit() # Kill mainloop 

def OnClosing(event = None):
	""" This function is to be called when the window is closed."""
	myMessage.set("{quit}")
	send()

################## --> INTERFACE <-- ######################

root = Tk() # create root window
root.title("Live Chat")
root.maxsize(900, 600) # width x height
root.config(bg="#DDDDDD")
img = Image.open("liveChat.jpg")
img = img.resize((300, 400), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)
messagesFrame = Frame(root) # Create a frame for holding the list of messages.

myMessage = StringVar() # Create a string variable, primarily for storing the value we get from the input field.
scrollbar = Scrollbar(messagesFrame) # To navigate through past messages.

messageList = Listbox(messagesFrame, bg='white', height = 20, width = 100, yscrollcommand=scrollbar.set)
panel = Label(root, image=img)
login = Label(panel, text="ENTER YOUR NAME")

scrollbar.pack(side = RIGHT, fill = Y)
messageList.pack(side = LEFT, fill = BOTH) 
panel.pack(side= RIGHT,fill =BOTH)
messagesFrame.pack(padx = 10, pady = 10)

name = StringVar() # Create a string variable, primarily for storing the value we get from the input field.
name.set("")
scrollbar = Scrollbar(messagesFrame) # To navigate through past messages.
entryName = Entry(panel, bd = 4, width = 30, textvariable = name)
entryName.bind("<Return>", Send)
login.pack(side= TOP,fill =X)
entryName.pack(side = TOP, fill = X, padx = 10)

entryField = Entry(root, bd = 4, width = 90, textvariable = myMessage)
entryField.bind("<Return>", Send)
entryField.pack(side = LEFT, fill = X, padx = 10,pady = 10)

buttonImg = itk.Image.open("send.jpg")

buttonImg = buttonImg.resize((30, 15), Image.ANTIALIAS)

buttonImg = itk.PhotoImage(buttonImg) 

sendButton = Button(root, bd = 2, bg='white' , width = 30, height=20, image = buttonImg , command = Send)
sendButton.pack(side = RIGHT, fill = X, padx = 10)

root.protocol("WM_DELETE_WINDOW", OnClosing)

###################################3#########################

#Host = input('Enter host: ')
#Port = input('Enter port: ')

Host = 'localhost'
Port = 33000
if not Port:
	Port = 33000 # Default value.
else:
	Port = int(Port)

BufSize = 1024
Addr = (Host, Port)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(Addr)

receiveThread = Thread(target = Receive)
receiveThread.start()
mainloop() # Starts GUI execution.
