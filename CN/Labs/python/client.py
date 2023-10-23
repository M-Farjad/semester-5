import socket
host ='127.0.0.1'
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("Enter message: ")
while message != 'bye':
    obj.send(message.encode())
    data = obj.recv(1024).decode()
    print("Received from server: " + str(data))
    message = input("Enter message: ")
    obj.send(message.encode())
obj.close()