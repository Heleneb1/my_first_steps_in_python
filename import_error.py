#Pour importer depuis un atre fichier python
# import operations

# print(operations.sum(1, 2))

#on peut aussi importer une fonction spécifique
# from operations import sum
# print(sum(1, 2))

#on peut aussi importer plusieurs fonctions
#from operations import sum, substract

#Docstring
def somme(a, b):
    """
    Cette fonction calcule la somme de deux nombres et retourne le résultat.

    Parameters:
    a (int): le premier nombre
    b (int): le deuxième nombre

    Returns:
    int: la somme de a et b
    """
    return a + b
help(somme)

#pour afficher la docstring
 #help(somme) dans la console #ou print(somme.__doc__)


#lever les erreurs try/except
#exemple
numerateur = int(input("Entrez le numérateur: "))
denominateur = int(input("Entrez le dénominateur: "))


try:
    resultat = numerateur / denominateur
    print(f"Le résultat de la division est: {resultat}")
except ZeroDivisionError:
    print("Le dénominateur ne doit pas être égal à zéro.")
except ValueError:
    print("Vous devez entrer un nombre entier.")
