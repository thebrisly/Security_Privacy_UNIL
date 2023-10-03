letter_frequency_english =  {'e' : 12.0, 't' : 9.10, 'a' : 8.12, 'o' : 7.68, 'i' : 7.31, 'n' : 6.95, 's' : 6.28, 'r' : 6.02, 'h' : 5.92, 'd' : 4.32, 'l' : 3.98, 'u' : 2.88, 'c' : 2.71, 'm' : 2.61, 'f' : 2.30, 'y' : 2.11, 'w' : 2.09, 'g' : 2.03, 'p' : 1.82, 'b' : 1.49, 'v' : 1.11, 'k' : 0.69, 'x' : 0.17, 'q' : 0.11, 'j' : 0.10, 'z' : 0.07 }

with open('ciphertext.txt', 'r') as file:
    ciphertext = file.read()

letter_counts = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}

# Function to decrypt the text with a found shift
def decrypt(text, shift):
    decrypted_text = ""
    for char in text :
        if char.isalpha() :
            if char.isupper() :
                char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            elif char.islower() :
                char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        decrypted_text += char
    return decrypted_text

# Counting how many letters there are (how many A's, B's, etc...) in the ciphertext to find the most frequent letter
for char in ciphertext.lower():
    if char in letter_counts:
        letter_counts[char] += 1
most_frequent_letter = max(letter_counts, key=letter_counts.get)

# Find the most accurate shift
best_shift = (ord(most_frequent_letter) - ord('e')) % 26


# Decrypt the text with the most accurate shift
decrypted_text = decrypt(ciphertext, best_shift)

# Result
print("The most likely shift :", best_shift)
print("The decrypted text:", decrypted_text)
