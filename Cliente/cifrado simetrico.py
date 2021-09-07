#pip install cryptography
from cryptography.fernet import Fernet

#Crear y guardar la llave
key = Fernet.generate_key()
#print('Llave:',key)
#with open('llave.key','wb') as archivo_key:
    #archivo_key.write(key)
    #archivo_key.close()
    
#Leer la clave
llave = open('llave.key','rb')

#Mensaje a encriptar
mensaje = 'Secreto no compartir con nadie mas'
print('Mensaje a encriptar-->',mensaje)
mensaje = mensaje.encode()
print(mensaje)

#Metodo Fernet
f = Fernet(key)

#Encriptar
#encriptado = f.encrypt(mensaje)
#print('Mensaje encriptado:')
#print(encriptado)

#Desencriptar
#desencriptado = f.decrypt(encriptado)
#desencriptado = desencriptado.decode()
#print('Mensaje desencriptado:')
#print(desencriptado)

#------------------------------------
#Encriptar archivo
file = open('prueba.txt', 'rb')
archivo = file.read()
encrypted_file = f.encrypt(archivo)
file.close()
file = open('prueba.txt', 'wb')
file.write(encrypted_file)
file.close()

#Desencriptar archivo
def desencript():
    file = open('prueba.txt', 'rb')
    encrypted_file = file.read()
    print(encrypted_file)
    decrypted_file = f.decrypt(encrypted_file)
    file.close()
    file = open('prueba.txt', 'wb')
    file.write(decrypted_file)
    file.close()
