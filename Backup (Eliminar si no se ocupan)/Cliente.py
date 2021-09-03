import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002)) #192.168.1.252

print('Enviando')
file = open('imagen_ori.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    #print('...')
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()
print('Exito')

#------------------------------------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002)) #192.168.1.252

print('Pidiendo imagen')
file = open('imagen_comparar.jpg', 'wb')
image_part = client.recv(2048)
print('Recibiendo')
while image_part:
    #print('...')
    file.write(image_part)
    image_part = client.recv(2048)

file.close()
client.close()
print('Exito')
#---------------------------------------------
