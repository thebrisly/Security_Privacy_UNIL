import enchant as e

with open('ciphertext.txt', 'r') as file:
    ciphertext = file.read()

d = e.Dict("en_US")

sub_words = ciphertext.split()

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

for shift in range(26):
    decrypted_text = ""
    for word in sub_words:
        decrypted_word = decrypt(word, shift)
        decrypted_text += decrypted_word + " "
    
    if all(d.check(word) for word in decrypted_text.split()):
        print("Décalage trouvé :", shift)
        print("Texte déchiffré :", decrypted_text)
        break

## this code is just to understand how enchant works.
#d = e.Dict("en_US")
#candidate_word = "cookie"
#print(d.check(candidate_word)) # True
#candidate_word = "lskvd"
#print(d.check(candidate_word)) # False

