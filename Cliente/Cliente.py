import socket
from cryptography.fernet import Fernet

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002))

#AQUI VA EL CIFRADO SIMETRICO

#Crear y guardar la llave
#key = Fernet.generate_key()
#print('Llave:',key)
#with open('llave.key','wb') as archivo_key:
    #archivo_key.write(key)
    #archivo_key.close()

#Leer la clave
llave = open('llave.key','rb')

#Metodo Fernet
f = Fernet(llave)

#Encriptar archivo
file = open('imgOriginal.jpg', 'rb')
archivo = file.read()
encrypted_file = f.encrypt(archivo)
file.close()
file = open('imgOriginal.jpg', 'wb')
file.write(encrypted_file)
file.close()

#Aquí enviamos la imagen encriptada
print('Enviando')
file = open('imgOriginal.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    #print('...')
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()
print('Exito')
#AQUI TERMINA DE ENVIAR LA IMAGEN CIFRADA


#------------------------------------------
#SE RECIBE LA IMAGEN DESCIFRADA
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

#AQUÍ VA LA COMPARACIÓN
#---------------------------------------------
