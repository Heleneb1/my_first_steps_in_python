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
#TODO revoir la pizza avec les classes et surtout les méthodes 
class Pizza:
    def __init__(self, ingredients, base, prix, type, diametre):
        self.ingredients = ingredients
        self.base = base
        self.prix = prix
        self.type = type
        self.diametre = diametre

    def preparer_pizza(self):
        print(f"Préparation de la pizza {self.type} avec {self.ingredients} sur une base {self.base} de diamètre {self.diametre} cm")
    def cuire_pizza(self):
        print("Cuisson de la pizza")
    def livrer_pizza(self):
        print(f"Livraison de la pizza {self.type} au prix de {self.prix} €")

base= input("Entrez la base de la pizza: (tomate ou blanche) ")
ingredients = input("Entrez les ingrédients de la pizza: (separés par des virgules) ")
diametre = input("Entrez le diamètre de la pizza, moyenne ou grande :")

taille = 30
if diametre == "grande":
    taille = 40

ingredients = ingredients.split(",")#transforme la chaine de caractères en liste   
prix = 10 + len(ingredients) 
pizza = Pizza(ingredients, base, prix, "Reine", taille)