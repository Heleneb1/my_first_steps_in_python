# Title: Distinction
average = input("Entrer votre moyenne : ")

if len(average) == 0:
    print("Vous n'avez pas entré de moyenne")
    
else:
    average = float(average)  # Convertir l'entrée en nombre

    if 12<=average <14:
        print("Mention assez bien")
    elif 14<=average <16:
        print("Mention bien")
    elif 16<=average <18:
        print("Mention très bien")
    elif average >= 18:
        print("Félicitations du jury")
    else:
        print("Sans mention")

print("Fin du programme")

# average = input("Entrer votre moyenne : ")
average = float(input("Entrer votre moyenne : "))  # Convertir l'entrée en nombre
# if len(average) == 0: # la fonction len() permet de connaitre la longueur d'une chaine de caractère ne fonctionne pas avec les nombres flottants
#     print("Vous n'avez pas entré de moyenne")
    
# else:
    # average = float(average)  # Convertir l'entrée en nombre
if 12<=average <14:
        print("Mention assez bien")
elif 14<=average <16:
        print("Mention bien")
elif 16<=average <18:
        print("Mention très bien")
elif average >= 18:
        print("Félicitations du jury")
else:
        print("Sans mention")

print("Fin du programme")
