# Load the required libraries/modules
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# TODO open the key file using the python open() function. Hint: use 'rb' as a parameter to read the file in binary
key_file = open("key", "rb")
key = key_file.read()
key_file.close()


# TODO open the encrypted image
image_file = open("encrypted_image", "rb")
encrypted_image = image_file.read()
image_file.close()


# TODO decrypt the image.
# The image was encrypted using AES encryption in the Electronic CodeBook mode of operation
# https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/

decrypted_image = Cipher(algorithms.AES(key), modes.ECB())
decryptor = decrypted_image.decryptor()


# TODO save the decrypted image in the image binary variable.
image_binary = decryptor.update(encrypted_image) + decryptor.finalize()


# TODO Save the image in jpg format
image_decrypted = open("decrypted_image.jpg", "wb")
image_decrypted.write(image_binary)
image_decrypted.close()

print("Image decrypted and saved as decrypted.jpg")

