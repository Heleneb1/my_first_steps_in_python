# Charger des données signifie transférer des données de fichiers vers le code ou inversement.
# Chargez des données avec les fonctions intégrées de Python
# Pour lire et écrire un fichier, vous pouvez utiliser la fonction intégrée   open()  , qui requiert deux paramètres : le nom du fichier et le mode. 

# Nom du fichier : le chemin d’accès au fichier que vous voulez lire ou dans lequel vous voulez écrire.

# Mode : le mode que vous voulez utiliser pour le fichier. Les options principales sont :

# Lire :   "r"

# Écrire (écraser) :   "w"

# Continuer d’écrire :   "a"

# Lire et écrire (sans écraser) :   "r+"


with open("file.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)
# Vous pouvez également utiliser la méthode   read()   pour lire tout le contenu d’un fichier en une seule fois.

# Par exemple, pour lire le contenu du fichier   file.txt   :


with open("file.txt") as fichier:
    contenu = fichier.read()
    print(contenu)

# Pour un csv
import csv

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',') # On utilise DictReader pour avoir les headers
    for ligne in reader:
        print(ligne)

# Pour un csv avec des headers on peut accéder aux valeurs par leur nom

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',') # On utilise DictReader pour avoir les headers
    for ligne in reader:
        print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])

# Pour écrire dans un fichier, vous pouvez utiliser la méthode   write()   :
en_tete = ["nom", "metier", "couleur_preferee"]
valeurs = [
    ["Alice", "ingénieure", "bleu"],
    ["Bob", "développeur", "rouge"],
    ["Charlie", "designer", "vert"]
]
with open('couleurs_preferees.csv', mode='w') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(en_tete)
    for valeur in valeurs:
        writer.writerow(valeur)
# ouvrir le fichier excel, selectionner les données, à partir d'un fichier text/csv ouvrir le fichier en .csv

# Les sites web n’ont pas tous des politiques qui autorisent d’extraire leurs données. Pour savoir si une entreprise l’autorise, assurez-vous de vérifier ses conditions générales.

# Pour de nombreux sites, ceux-ci sont disponibles sur leur fichier robots.txt. Vous pouvez ajouter « /robots.txt » après l’URL du site pour voir s’ils en ont un.

# Pour extraire des données d’un site web, vous pouvez utiliser des bibliothèques comme BeautifulSoup et requests.

# Il y a des problèmes légitimes sur l’éthique et la confidentialité quand on extrait des données web.

# N’extrayez jamais les données personnelles de qui que ce soit, ou d’un site qui ne l’autorise pas.

# Comme internet est en constante évolution, les scripts d’extraction de données web nécessitent d’être mis à jour.

# on appelle cela le web scraping 
