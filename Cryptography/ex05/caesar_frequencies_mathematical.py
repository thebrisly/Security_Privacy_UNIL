## NOTE ##
# I didn't code this one. ChatGPT did. Just wanted to see the difference :)

# Charger les fréquences de lettres en anglais depuis le fichier frequencies.py
from frequencies import letter_frequency_english

# Charger le texte chiffré (vous devrez l'obtenir à partir de votre source)
ciphertext = "vq dflk fr mvnl nlnz uvbn dz zqj oqn mvml vq dflk mvnu"  # Exemple de texte chiffré

# Fonction pour déchiffrer le texte avec un décalage donné
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

# Fonction pour calculer la distance entre les fréquences des lettres du texte et l'anglais
def calculate_distance(text, letter_frequencies):
    text = text.lower()
    observed_frequencies = {letter: 0 for letter in letter_frequencies}
    total_letters = 0

    for char in text:
        if char in letter_frequencies:
            observed_frequencies[char] += 1
            total_letters += 1

    if total_letters == 0:
        return float("inf")

    distance = 0
    for letter, frequency in letter_frequencies.items():
        expected_frequency = frequency / 100  # Convertir en décimal
        observed_frequency = observed_frequencies[letter] / total_letters
        distance += (expected_frequency - observed_frequency) ** 2

    return distance

# Analyse de fréquence et recherche du décalage le plus probable
best_shift = 0
best_score = float("inf")

for shift in range(26):
    decrypted_text = decrypt(ciphertext, shift)
    
    # Calculer la distance entre les fréquences des lettres du texte déchiffré et l'anglais
    score = calculate_distance(decrypted_text, letter_frequency_english)
    
    # Trouver le décalage qui minimise le score
    if score < best_score:
        best_score = score
        best_shift = shift

# Déchiffrer le texte avec le décalage le plus probable
decrypted_text = decrypt(ciphertext, best_shift)

# Afficher le résultat
print("Décalage le plus probable :", best_shift)
print("Texte déchiffré :", decrypted_text)