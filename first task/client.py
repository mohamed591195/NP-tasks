from socket import *

s = socket(AF_INET, SOCK_STREAM)

port = 5000

s.connect(('127.0.0.1', port))
print(s.recv(1024))


try:
    while True:
        # taking the message from terminal and determining its length (every char=1byte)
        message = "from client to server: {}".format(input("message to send to server: "))
        message_length = len(message)

        #sending the length of the message as a first step
        s.send(message_length.to_bytes(4, 'big'))
        #appending it by a next send with the message data
        s.send(message.encode('utf-8'))
except:
    s.close()