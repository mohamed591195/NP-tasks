'''
server availabe only for one client to connect
'''

from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("socket successfully created!")

port = 5000 

s.bind(('127.0.0.1', port))
print("socket binded to port ", port)

# the max number of queued connections
s.listen(5)
print("socket is listening")


client, address = s.accept()
print(f"got connection from address {address}")

client.send(b"Thank you for connection")

while True:
    try:
        # receiving the message length first
        message_length = int.from_bytes(client.recv(4), 'big')
        # using the message length as a buffer to receive the data
        message = client.recv(message_length)
        # print('message_length: ', message_length)
        print(message.decode('utf-8'))
    except:
        client.close()
        s.close()

    