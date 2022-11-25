# Server Side Script
# Supports Python v3.*
from socket import *
server_port = 8008
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)
print ("Welcome: The server is now ready to receive")
connection_socket, address = server_socket.accept()
while True:
  sentence = connection_socket.recv(2048).decode()
  print('>> ',sentence)
  if(sentence == 'q'):
    break
  message = input(">> ")
  connection_socket.send(message.encode())
connection_socket.close()



# Client Side Script
# Supports Python v3.*

from socket import *
server_name = 'localhost'
server_port = 8008
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print (">> ", message.decode())
  if(message == 'q'):
    break
client_socket.close()
