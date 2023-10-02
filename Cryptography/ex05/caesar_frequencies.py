letter_frequency_english =  {'e' : 12.0, 't' : 9.10, 'a' : 8.12, 'o' : 7.68, 'i' : 7.31, 'n' : 6.95, 's' : 6.28, 'r' : 6.02, 'h' : 5.92, 'd' : 4.32, 'l' : 3.98, 'u' : 2.88, 'c' : 2.71, 'm' : 2.61, 'f' : 2.30, 'y' : 2.11, 'w' : 2.09, 'g' : 2.03, 'p' : 1.82, 'b' : 1.49, 'v' : 1.11, 'k' : 0.69, 'x' : 0.17, 'q' : 0.11, 'j' : 0.10, 'z' : 0.07 }

with open('ciphertext.txt', 'r') as file:
    ciphertext = file.read()


# Function to decrypt the text with a found shift
def decrypt(text, shift):
    

    return decrypted_text

# Function to calculate the distance between frequencies and letters of the ciphertext
def calculate_distance(text, letter_frequencies):
    
    return distance

# Find the most accurate shift
best_shift = 


# Decrypt the text with the most accurate shift
decrypted_text = decrypt(ciphertext, best_shift)

# Result
print("The most likely shift :", best_shift)
print("The decrypted text:", decrypted_text)
