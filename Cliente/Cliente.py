import socket
from cryptography.fernet import Fernet
import cv2 #Es la libreria de OpenCV. Se debe instalar con el comando "pip install opencv-contrib-python"
import numpy as np
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002))

#Leer la clave
llave = open('llave.key','rb').read()

#Metodo Fernet
f = Fernet(llave)

#Encriptar archivo
file = open('imgOriginal.jpg', 'rb')
archivo = file.read()
encrypted_file = f.encrypt(archivo)
file.close()
file = open('imgOriginalEnc.jpg', 'wb')
file.write(encrypted_file)
file.close()

# #Aquí enviamos la imagen encriptada
print('Enviando')
file = open('imgOriginalEnc.jpg', 'rb')
image_data = file.read(2048)

while image_data:
    client.send(image_data)
    image_data = file.read(2048)

file.close()
client.close()
print('Exito')

#------------------------------------------
#SE RECIBE LA IMAGEN DESCIFRADA
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002)) #192.168.1.252

print('Pidiendo imagen')
file = open('imagen_cop.jpg', 'wb')
image_part = client.recv(2048)
print('Recibiendo')
while image_part:
    file.write(image_part)
    image_part = client.recv(2048)

file.close()
client.close()
print('Exito')

#---------------------------------------------

#Cargamos las imagenes a comparar, se pasa el nombre del archivo y el 1 es para leer la imagen a color
imagen1 = cv2.imread("imgOriginal.jpg",1)
imagen2 = cv2.imread("imagen_cop.jpg",1)#Imagen descifrada

def comparar(img1,img2):
    diferencia = cv2.subtract(img1,img2)#Lee los arreglos de pixeles de cada imagen y los compara haciendo una resta.
    if not np.any(diferencia):
        print("Las imagenes son iguales")
        #Mostar las dos imagenes
        imas = np.hstack((imagen1,imagen2))#Toma las imagenes a visualizar de forma conjunta
        cv2.imshow("Photo", imas)
        cv2.waitKey(0)
    else:
        cv2.imwrite("img_diferencia.jpg",diferencia) #Se crea una imagen con las diferencias encontradas
        imagenDiferente = cv2.imread('img_diferencia.jpg')
        print("Las imagenes son distintas")
        #Mostar las imagenes
        ima = np.hstack((imagen1, imagenDiferente, imagen2))
        cv2.imshow("Photo", ima)
        cv2.waitKey(0)

comparar(imagen1,imagen2)