import cv2 #Es la libreria de OpenCV. Se debe instalar con el comando "pip install opencv-contrib-python"
import numpy as np
import os

os.chdir('./img')#Se posiciona en el directorio donde se encuentran las imagenes

#Cargamos las imagenes a comparar, se pasa el nombre del archivo y el 1 es para leer la imagen a color
imagen1 = cv2.imread("imgOriginal.jpg",1)
imagen2 = cv2.imread("imgOriginalCopia.jpg",1)#Imagen Identica
imagen3 = cv2.imread("imgDistinta.jpg",1)#Imagen con un pequeño cambio de color en un pixel

#Función de comparación
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
        #Mostar las dos imagenes
        ima = np.hstack((imagen1, imagenDiferente, imagen3))
        cv2.imshow("Photo", ima)
        cv2.waitKey(0)

#Se realiza la comparación con imagenes iguales
# comparar(imagen1,imagen2)

#Se realiza la comparación con imagenes distintas
comparar(imagen1,imagen3)

