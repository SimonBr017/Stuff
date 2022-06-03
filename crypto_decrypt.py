#!/usr/bin/python3
"""Crypt et décrypt des fichier grasse à
la génération d'une clé de chifrement ou
l'utilisation d'une clé déja existente"""

import time
from cryptography.fernet import Fernet

def encryption():
	"""génére une clé l'enregistre en tant que
	filekey.key. Encrypte le contenu d'un fichier avec la clé"""

	filekey_name = input("filekey name > ")
	#récupére la clé dans le fichier si il existe
	try:
		with open(filekey_name, 'rb') as filekey:
			key = filekey.read()
		print("")
		print("Clé trouvé")
		time.sleep(2)

	#Sinon génére la clé et la stock dans filekey.key
	except:
		print("")
		print("Pas de fichier filekey.key trouvé")
		time.sleep(1)
		print("")
		print("Génération d'une nouvelle clé")
		time.sleep(1)
		key = Fernet.generate_key()
		with open(filekey_name, 'wb') as filekey: 
			filekey.write(key)
		print("")
		print("Sauvegarde dans ", filekey_name)
		time.sleep(2)

	fernet = Fernet(key)

	#lit le fichier original
	print("")
	filename = input("filename > ")
	with open(filename, 'rb') as file:
		original =file.read()
	
	#encrypt le contenu
	encrypt_var = fernet.encrypt(original)

	#ré-écrit dans un nouveau fiichier
	with open("encrypt_"+filename, 'wb') as encrypt_file:
		encrypt_file.write(encrypt_var)
	print("")
	print("Création d'un nouveau fichier Encrypt_" + filename)
	time.sleep(1)
	print('Success')


def decryption():
    """Decrypt un fichier à partir d'une clé
    de chiffrement fournit dans un fichier"""

	#definit le nom de fichier contenant la clé de chifrement
    filekey_name = input("filekey name > ")
    try:
        with open(filekey_name, 'rb') as filekey:
            key = filekey.read()
    except:
        print("")
        print("Erreur Nom de Fichier incorect, j'ai la flem ducoup ->> CRACH")
        exit
    
    fernet = Fernet(key)
    
    file_to_decrypt_name = input("File to Decrypt name > ")
    with open(file_to_decrypt_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    
    #sauvegarde le contenue décrypté dans un nouveau fichier
    decrypt_file_name = "decrypted_"+ file_to_decrypt_name
    with open(decrypt_file_name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        print("")
        print("Création d'u nouveau Fichier")
        print("le Fichier est décrypté")
        print("")
        time.sleep(2)

if __name__ == '__main__':

	i = 0

	while i == 0:
		print("What Do You Whant ?")    
		process = input("Encrypt or Decrypt > ")
		if process == "Encrypt" or process == "encrypt":
			encryption()
			i +=1
		if process == "Decrypt" or process == "decrypt":
			decryption()
			i +=1
		if process == "exit":
			i +=1
		else:
			i += 0

		print("")
		print("New Run ?")
		rep = input("Yes or No > ")
		if rep == "Yes" or rep == "yes" or rep == "y" or rep == "Y":
			i -= 1
		else:
			exit