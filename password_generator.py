# En cas d'import, les placer par ordre alphabétique et les séparer des modules de la bibliothèque standard par une ligne vide en haut et en bas.

# Exemple d'utilisation du module random
# print(random.randint(1, 100))  # Génère un entier aléatoire entre 1 et 100 inclus
# print(random.choice("abcdefghijklmnopqrstuvwxyz"))  # Choisit un caractère aléatoire dans la chaîne de caractères
# print(random.random())  # Génère un nombre aléatoire flottant entre 0 et 1

# random() : Pour des valeurs aléatoires classiques, non sécurisées. Utile pour des jeux ou des simulations.
# Méthodes courantes :
# - random.random() : Renvoie un flottant entre 0 et 1.
# - random.randint(a, b) : Renvoie un entier aléatoire entre a et b inclus.
# - random.choice(seq) : Renvoie un élément choisi aléatoirement dans une séquence (par ex., liste).

# secrets() : Pour des valeurs aléatoires sécurisées (mots de passe, tokens). Idéal pour la cryptographie.
# Méthodes courantes :
# - secrets.randbelow(n) : Renvoie un entier aléatoire entre 0 et n-1.
# - secrets.choice(seq) : Renvoie un élément choisi de manière sécurisée dans une séquence.
# Avantage : Les valeurs générées par secrets sont plus difficiles à prédire, ce qui les rend plus sûres pour les applications sensibles.

# Expressions régulières
# pattern = 'l+' : Correspond à une ou plusieurs occurrences consécutives de la lettre 'l'.
# quote = 'Not all those who wander are lost.'
# print(re.search(pattern, quote))  # Renvoie le premier match trouvé pour 'l', par exemple : <re.Match object; span=(4, 5), match='l'>

# pattern = 'w[ha]' : Correspond à 'w' suivi de 'h' ou 'a'.
# quote = 'Not all those who wander are lost.'
# print(re.findall(pattern, quote))  # Renvoie toutes les occurrences correspondant à 'w' suivi de 'h' ou 'a', par exemple : ['wa']

# pattern = '.+' : Correspond à une ou plusieurs occurrences de n'importe quel caractère sauf les nouvelles lignes.
# pattern = '\.' : Correspond spécifiquement au caractère point '.'.
# quote = 'Not all those who wander are lost.'
# print(re.findall(pattern, quote))  # Utilisation de '.+' ou '\.' pour trouver les occurrences correspondantes.
# Le motif r'\.' en Python correspond précisément au caractère point .. Voici comment il fonctionne en détail :

# r'' : Le préfixe r signifie "raw string" (chaîne brute). Il permet à Python d'interpréter les backslashes (\) littéralement, sans les traiter comme des caractères d'échappement.
# Donc, en utilisant pattern = r'\.', tu cherches toutes les occurrences du caractère point (.) dans une chaîne de caractères.
# \d : Correspond à un chiffre décimal (0-9). remplace [0-9] 

# Dans une classe de caractères, tu peux combiner plusieurs plages en les écrivant simplement les unes après les autres dans les crochets, sans caractères supplémentaires. Par exemple, [a-d3-6] est la combinaison de [a-d] et [3-6].

# Maintenant, modifie le dernier motif regex pour qu'il corresponde à n'importe quel caractère non alphanumérique. Combine les plages a-z, A-Z et 0-9 en une seule classe de caractères, puis ajoute ^ en premier caractère pour nier le motif.

# Cela donnerait : [^a-zA-Z0-9], qui correspond à tous les caractères non alphanumériques. ou '\W'

import re  # Import du module re pour utiliser les expressions régulières
import secrets  # Import du module secrets pour générer des valeurs aléatoires sécurisées
import string  # Import du module string pour obtenir des ensembles de caractères prédéfinis (comme les lettres et chiffres)

# Fonction pour générer un mot de passe sécurisé avec des contraintes sur le type de caractères
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Définir les caractères possibles pour le mot de passe
    letters = string.ascii_letters  # Toutes les lettres (majuscules et minuscules)
    digits = string.digits          # Tous les chiffres (de '0' à '9')
    symbols = string.punctuation     # Tous les symboles de ponctuation (par ex., '!', '@', '#', etc.)

    # Combiner tous les types de caractères dans une seule chaîne
    all_characters = letters + digits + symbols

    # Boucle pour générer un mot de passe respectant les contraintes spécifiées
    while True:
        password = ''  # Initialise le mot de passe vide
        # Générer le mot de passe en ajoutant des caractères aléatoires
        for _ in range(length):
            password += secrets.choice(all_characters)  # Ajoute un caractère choisi aléatoirement

        # Définir les contraintes de composition du mot de passe sous forme de tuples (quantité, pattern)
        constraints = [
            (nums, r'\d'),              # Vérifier qu'il y a au moins 'nums' chiffres (d représente les chiffres)
            (special_chars, fr'[{symbols}]'),  # Vérifier qu'il y a au moins 'special_chars' caractères spéciaux
            (uppercase, r'[A-Z]'),      # Vérifier qu'il y a au moins 'uppercase' majuscules
            (lowercase, r'[a-z]')       # Vérifier qu'il y a au moins 'lowercase' minuscules
        ]

        # Vérifie que chaque contrainte est respectée dans le mot de passe
        if all(
            constraint <= len(re.findall(pattern, password))  # Compte les occurrences pour chaque pattern
            for constraint, pattern in constraints            # constraint est le minimum requis pour chaque type
        ):
            break  # Si toutes les contraintes sont respectées, on arrête la boucle

    return password  # Retourne le mot de passe qui respecte toutes les contraintes

# Si le script est exécuté directement, génère un mot de passe
if __name__ == '__main__':
    new_password = generate_password()  # Appelle la fonction pour générer le mot de passe
    print('Generated password:', new_password)  # Affiche le mot de passe généré
