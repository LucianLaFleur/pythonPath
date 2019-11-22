#!/user/bin/python3

# example tcp server
 import socket
#  af inet means you're using IPV4 with TCP (socket family, socket type)
 serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  store host name, get the address info
host = socket.gethostname()
# Can make any port connection here
port = 444
# connect an address to a socket with "bind()"
serversocket.bind((host, port))

# look for 3 connections with the listener
serversocket.listen(3)

while True:
  # get data from client you're connected to
  clientsocket, address = serversocket.accept

  print("recieved connection from " + str(address))

  message = "placeholder message for connection getting established" + "\r\n"
  # send the message var to the connected client
  clientsocket.send(message)
  # close the connection
  clientsocket.close()