#Une classe est un modèle pour créer des objets. Un objet a des propriétés et des méthodes (fonctions) associées à cet objet. Presque tout en Python est un objet, avec ses propriétés et ses méthodes. Un objet est une instance d'une classe.
#Une classe est définie en utilisant le mot-clé class.
#Créer une classe
#Pour créer une classe, utilisez le mot-clé class:

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee #self est un paramètre obligatoire qui fait référence à l'objet lui-même et est utilisé pour accéder aux variables qui appartiennent à la classe.    
   

    def klaxonner(self):
        print("Bip Bip")
Cybertruck = Voiture("Tesla", "Cybertruck", 2024)
corrola = Voiture("Toyota", "Corrola", 2022)
print(Cybertruck.marque)
Cybertruck.klaxonner()
Cybertruck.annee = 2025
print(Cybertruck.annee)
print(corrola.annee)
#La méthode __init__() est une méthode spéciale, elle est toujours appelée lorsque la classe est instanciée.
#Les paramètres de la méthode __init__() sont les propriétés de la classe.
#La méthode __init__() est appelée automatiquement chaque fois que la classe est utilisée pour créer un nouvel objet.
#Les objets peuvent également contenir des méthodes. Les méthodes dans les objets sont des fonctions qui appartiennent à l'objet.
#Créer un objet

#Python grand nombre
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
a = 1_000_000_000_000_000
b= 2_500
print(a*b)
print(f"{a*b:,}") #permet d'afficher un grand nombre avec des séparateurs de milliers par des virgules
print(f"{a*b:n}")#permet d'afficher un grand nombre avec des séparateurs de milliers par des espaces


