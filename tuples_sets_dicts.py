#Tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)#affiche le tuple
print(type(numbers))#<class 'tuple'>
print(2 in numbers)#true
print(6 in numbers)#false
print(numbers[0])#affiche le premier élément du tuple
print(numbers.count(2))#compte le nombre d'occurence de l'élément 2
print(numbers.index(2))#affiche l'index de l'élément 2

#Si on veut utiliser un tuple pour stocker des éléments qui ne changeront pas , si des éléments sont différents on a tendance à utiliser un tuple

#Set
numbers = {1, 3, 4, 5, 2, 2,5}#les éléments sont uniques
print(numbers)#affiche le set sans les doublons il est trié est immuable
print(type(numbers))#<class 'set'>
print(2 in numbers)#true
print(len(numbers))#affiche la taille du set
numbers.add(6)#ajoute un élément au set on ne peut pas acceder à l'index des éléments du set on ne peut pas modifier les éléments du set
print(numbers)
numbers.remove(6)#supprime un élément du set
#on peut retirer le premier élément du set
numbers.pop()
#on peut convertir un set en liste
numbers = list(numbers)

print(numbers)
numbers.clear()#vide le set
print(numbers)
#Si on veut utiliser un set pour stocker des éléments uniques et qu'on ne veut pas les modifier

#on peut comparer 2 sets pour voir s'ils ont des éléments en commun
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))#affiche les éléments communs
print(set1.union(set2))#affiche les éléments des deux sets
print(set1.difference(set2))#affiche les éléments qui sont dans le premier set mais pas dans le deuxième

#Pour voir toutes les méthodes disponibles pour un set
#print(dir(set1))
#Pour voir l'aide sur une méthode
#print(help(set1.intersection))

#Dictionary 
#les dictionnaires sont des objets qui stockent des paires clé-valeur
#les clés sont uniques
#les valeurs peuvent être de différents types
#les dictionnaires sont mutables
#les dictionnaires sont non ordonnés
#les dictionnaires sont indexés
#les clés doivent être immuables
#les valeurs peuvent être mutables
#les clés sont souvent des chaines de caractères
#les dictionnaires sont souvent utilisés pour stocker des données structurées
#les dictionnaires sont souvent utilisés pour stocker des données de configuration
#les dictionnaires sont souvent utilisés pour stocker des données de base de données
#les dictionnaires sont souvent utilisés pour stocker des données de fichiers JSON
nombres = {"un": 1, "deux": 2, "trois": 3}
print(nombres)#affiche le dictionnaire
print(type(nombres))#<class 'dict'>
print("un" in nombres)#true
print(nombres["un"])#affiche la valeur de la clé "un"
print(nombres.get("un"))#affiche la valeur de la clé "un"
print(nombres.get("quatre"))#affiche None si la clé n'existe pas
print(nombres.get("quatre", "Pas de valeur"))#affiche "Pas de valeur" si la clé n'existe pas
print(nombres.keys())#affiche les clés du dictionnaire
print(nombres.values())#affiche les valeurs du dictionnaire
print(nombres.items())#affiche les clés et les valeurs du dictionnaire sous forme de tuples
print(len(nombres))#affiche la taille du dictionnaire
print(dir(nombres))#affiche les méthodes disponibles pour un dictionnaire
print(nombres.update({"quatre": 4}))#ajoute un élément au dictionnaire
