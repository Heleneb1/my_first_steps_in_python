# Bien sûr ! Analysons la ligne de code suivante :

# python
# Copier le code
# odd_digits = card_number_reversed[::2]
# Décomposition de la ligne de code
# card_number_reversed :

# Cette variable contient le numéro de carte de crédit qui a été inversé, c'est-à-dire que les chiffres sont disposés de droite à gauche. Par exemple, si card_number était "123456789", alors card_number_reversed serait "987654321".
# L’indexation avec des tranches (slicing) :

# En Python, on peut accéder à une sous-partie d'une séquence (comme une liste ou une chaîne de caractères) en utilisant la notation de tranchage, qui a la forme sequence[start:stop:step].🚨
# Dans ce cas, on utilise ::2, ce qui signifie que :
# start n'est pas spécifié, donc on commence à l'index 0 (le début de la séquence).
# stop n'est pas spécifié, donc on continue jusqu'à la fin de la séquence.
# step est 2, ce qui signifie que l'on va prendre chaque deuxième élément de la séquence.🚨

# Exemple d'application
# Pour mieux comprendre, prenons un exemple :

# Exemple :
# Imaginons que card_number_reversed soit la chaîne suivante :

# python
# Copier le code
# card_number_reversed = "987654321"
# Utiliser card_number_reversed[::2] donnerait :

# Résultat :
# On commence à l'index 0, on prend 9 (premier chiffre).
# On saute un chiffre (prend 8 à l'index 1) et on prend 7 à l'index 2.
# Ensuite, on prend 5 (index 4), puis 3 (index 6) et enfin 1 (index 8).
# Le résultat de card_number_reversed[::2] serait donc :

# python
# Copier le code
# "97531"
# Pourquoi l'utiliser ?
# Dans le contexte de la vérification d'un numéro de carte, les chiffres aux positions impaires (en partant de la droite, ou après inversion) sont souvent traités différemment des chiffres aux positions paires. Dans l'algorithme de Luhn, par exemple, on additionne les chiffres impairs et on applique un traitement particulier aux chiffres pairs.
# En résumé
# La ligne odd_digits = card_number_reversed[::2] extrait tous les chiffres qui se trouvent aux positions impaires (index 0, 2, 4, ...) de la chaîne inversée card_number_reversed, ce qui permet de les traiter séparément des chiffres aux positions paires. C'est une méthode efficace et concise pour obtenir ce qu'on appelle les "chiffres impairs" de la séquence.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
   
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()