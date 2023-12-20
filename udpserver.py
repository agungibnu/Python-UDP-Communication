import socket
from socketserver import UDPServer

localIp = "192.168.1.12"
localPort = 4444
bufferSize = 1024

# message to send back to client
msgFromServer = "Hello UDP Client\n"
byteToSend = str.encode(msgFromServer)
UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPSocket.bind((localIp, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while (1):
    print("listening")
    byteAddressPair = UDPSocket.recvfrom(bufferSize)
    print(byteAddressPair)
    message = byteAddressPair[0]
    

    address = byteAddressPair[1]
    clientMSG = "Message from client :{}".format(message.decode())
    clientIP = "Client IP :{}".format(address)


    print(clientMSG)
    print(clientIP)

    #sending reply to client
    UDPSocket.sendto(byteToSend, address)