import pandas as pd
from itertools import combinations

# Charger le jeu de données depuis un fichier CSV
data = pd.read_csv('records.csv')  # Assurez-vous de remplacer 'votre_dataset.csv' par le chemin correct.

# Attributs QID
qid_attributes = ["birth_year", "sex", "zipcode"]

# Initialiser les variables pour stocker la meilleure généralisation et la meilleure distortion
meilleure_generalisation = None
meilleure_distortion = float('inf')

# Générer toutes les combinaisons possibles d'attributs QID
qid_combinations = []
for r in range(1, len(qid_attributes) + 1):
    qid_combinations.extend(combinations(qid_attributes, r))

# Contrainte k >= 6
k_constraint = 6

# Loop à travers chaque combinaison QID
for qid_combination in qid_combinations:
    # Génération des données généralisées en utilisant la combinaison QID actuelle
    generalized_data = data.groupby(list(qid_combination)).size().reset_index(name='count')
    
    # Calcul de la distortion (dans cet exemple, distortion = nombre de groupes généralisés)
    distortion = len(generalized_data)
    
    # Vérifier si la distortion est inférieure à la meilleure jusqu'à présent
    if distortion < meilleure_distortion and len(generalized_data) >= k_constraint:
        meilleure_distortion = distortion
        meilleure_generalisation = qid_combination

# Imprimer la meilleure généralisation sous la forme de triplet sans espaces
meilleure_generalisation_format = tuple(int(attr in meilleure_generalisation) for attr in qid_attributes)
print(meilleure_generalisation_format)
