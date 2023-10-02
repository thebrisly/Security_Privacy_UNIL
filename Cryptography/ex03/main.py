# Load the required libraries/modules
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# TODO open the key file using the python open() function. Hint: use 'rb' as a parameter to read the file in binary
key_file = open("key", "rb")
key = key_file.read()
key_file.close()


# TODO open the encrypted image
# La fonction open() renvoie un objet file qui peut être utilisé pour lire, écrire et modifier le fichier.
# La fonction read() est utilisée pour lire le contenu d'un fichier déjà ouvert et stocke le contenu dans la variable (ici encrypted_image)
# Une fois que l'on a lu l'image et stocké le contenu qqpart on peut fermer le fichier de référence.
image_file = open("encrypted_image", "rb")
encrypted_image = image_file.read()
image_file.close()


# TODO decrypt the image.
# The image was encrypted using AES encryption in the Electronic CodeBook mode of operation
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

# Decryptor est utilisé pour effectuer réellement le processus de déchiffrement des données.
decrypted_image = (Cipher(algorithms.AES(key), modes.ECB())).decryptor()


# TODO save the decrypted image in the image binary variable.
image_binary = decrypted_image.update(encrypted_image) + decrypted_image.finalize()


# TODO Save the image in jpg format
image_decrypted = open("decrypted_image.jpg", "wb")
image_decrypted.write(image_binary)
image_decrypted.close()

print("Image decrypted and saved as decrypted.jpg")

