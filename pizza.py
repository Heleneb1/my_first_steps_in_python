#TODO revoir la pizza avec les classes et surtout les méthodes 
class Pizza:
    def __init__(self, ingredients, base, prix, style, diametre, table,adresse):
        self.ingredients = ingredients
        self.base = base
        self.prix = prix
        self.style = style
        self.diametre = diametre
        self.table = table
        self.adresse =adresse

    def preparer_pizza(self):
        print(f"Préparation de la pizza {self.style} avec {self.ingredients} sur une base {self.base} de diamètre {self.diametre} cm")
    def cuire_pizza(self):
        print("Cuisson de la pizza")
    def livrer_pizza(self):
        print(f"Livraison de la pizza {self.style} au prix de {self.prix} €")
    def add_ingredients(self, new_ingredients):
        if "ananas" in new_ingredients.lower():
            raise TypeError("Les ananas ne font pas partis des ingrédients")
        self.ingredients.append(new_ingredients)
        self.prix+=1
    def servir(self, table):
        print("Je sers la pizza a la table", table)

    def livrer(self, adresse):
        print(f"Je livre la pizza a l'adresse, {adresse}")

# Inputs utilisateur
base = input("Entrez la base de la pizza (tomate ou blanche) : ")
ingredients = input("Entrez les ingrédients de la pizza (séparés par des virgules) : ")
diametre = input("Entrez le diamètre de la pizza (moyenne ou grande) : ")
style = input("Entrez le style de pizza souhaité parmis: calzonne , romaine, napolitaine, végétarienne : ")
servir = input("Sur place ? (oui/non) : ")

# Gestion du diamètre
taille = 30
if diametre == "grande":
    taille = 40
elif diametre != "moyenne":  # Gestion des entrées incorrectes
    print("Diamètre inconnu, pizza par défaut en taille moyenne.")

table = None
adresse = None
if servir == "oui":
    table= input("Entrez le numero de table : ")
elif servir=="non":  
    adresse = input("Entrez l'adresse de livraison : ")

# Conversion de la liste d'ingrédients
ingredients = ingredients.split(",")  # Transforme la chaîne en liste
prix = 10 + len(ingredients)  # Prix de base + nombre d'ingrédients

pizza = Pizza(ingredients, base, prix, style, taille,table, adresse)

# Test des méthodes
pizza.preparer_pizza()
pizza.cuire_pizza()
if servir == "oui":
    pizza.servir(table)
else:
    pizza.livrer_pizza()

# Ajouter un nouvel ingrédient
nouvel_ingredient = input("Voulez-vous ajouter un ingrédient ? (oui/non) ")
if nouvel_ingredient.lower() == "oui":
    ingr = input("Quel ingrédient voulez-vous ajouter ? ")
    pizza.add_ingredients(ingr)
    print(f"Nouvel ingrédient ajouté : {ingr}. Nouveau prix : {pizza.prix} €")


# Convertir la liste d'ingrédients en chaîne
ingredients_str = ", ".join(pizza.ingredients)  # Transforme la liste en chaîne

pizza.preparer_pizza()
pizza.cuire_pizza()
print(f"Ingrédients : {pizza.ingredients}")
print(f"Prix : {pizza.prix} €")
print(f"Style : {pizza.style}")
print(f"Diamètre : {pizza.diametre} cm, base : {pizza.base}")
if servir == "oui":
    print(f"La pizza sera servie à la table : {pizza.table}")
else:
    print(f"La pizza sera livrée à l'adresse :{pizza.adresse}")
