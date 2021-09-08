import socket
from cryptography.fernet import Fernet


server = ''
client_socket=''
  #Metodo Fernet
f = Fernet(key)

def connect():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1002)) #192.168.1.252
    server.listen(1)
    print('Esperando')
    client_socket, client_address = server.accept()


def acept():
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


def readKey():
        #Leer la clave
    llave = open('llave.key','rb')

    #Mensaje a encriptar
    mensaje = 'Secreto no compartir con nadie mas'
    print('Mensaje a encriptar-->',mensaje)
    mensaje = mensaje.encode()
    print(mensaje)

  

#Desencriptar archivo
def desencript():
    file = open('imagen_cop.jpg', 'rb')
    encrypted_file = file.read()
    print(encrypted_file)
    decrypted_file = f.decrypt(encrypted_file)
    file.close()
    file = open('imagen_cop.jpg', 'wb')
    file.write(decrypted_file)
    file.close()

def communication():
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