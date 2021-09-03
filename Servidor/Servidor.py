import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1002)) #192.168.1.252
server.listen(1)

print('Esperando')

client_socket, client_address = server.accept()
#---------------------------------------------
file = open('imagen_cop.jpg', 'wb')
image_part = client_socket.recv(2048)
print('Recibiendo')
while image_part:
    print('...')
    file.write(image_part)
    image_part = client_socket.recv(2048)

file.close()
client_socket.close()
print('Exito')



#---------------------------------------------
client_socket, client_address = server.accept()
print('Enviando')
file = open('imagen_cop.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    #print('...')
    client_socket.send(image_data)
    image_data = file.read(2048)

file.close()
client_socket.close()
