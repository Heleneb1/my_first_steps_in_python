ma_liste= [1, 2, 3, 4, 5]
print("ma_liste")
print(type(ma_liste))
print(ma_liste[0])
ma_liste[0] = 6#on change la valeur de l'index 0
print(ma_liste[0])#on a changé la valeur de l'index 0
print(ma_liste[0:2])#affiche les éléments de l'index 0 à l'index 2
ma_liste.append(7)#ajoute un élément à la fin de la liste
print(ma_liste)
ma_liste.insert(1, 8)#ajoute un élément à l'index 1
print(ma_liste)
ma_liste.remove(8)#supprime l'élément 8
print(ma_liste)
print(len(ma_liste))#affiche la longueur de la liste
ma_liste.pop(2)#supprime l'élément à l'index 2

#boucle while
i = 0
while i < 5:
    print(i)
    i += 1 #incrémente i de 1 à chaque tour de boucle si on ne l'incrémente pas la boucle sera infinie

#boucle for
for i in range(5):
    print(i)
