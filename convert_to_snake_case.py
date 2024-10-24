# .strip() methode est utilisée pour supprimer les espaces blancs au début et à la fin d'une chaîne. On peut également spécifier les caractères à supprimer en passant un argument à la méthode. Voici un exemple :
# original_string = "_example_string_"

# clean_string = original_string.strip('_') retournera "example_string".

#list comprehension est une méthode concise pour créer des listes en Python. Elle est souvent utilisée pour transformer ou filtrer des listes existantes. Voici un exemple :
# numbers = [1, 2, 3, 4, 5] 
# squares = [number**2 for number in numbers]
# print(squares) retournera [1, 4, 9, 16, 25].
#le if se trouve après la boucle for dans la liste de compréhension. Cela permet de filtrer les éléments de la liste en fonction d'une condition. Voici un exemple :
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [number for number in numbers if number % 2 == 0]
# snake_cased_char_list = ['_' + char.lower() if char.isupper()else char for char in pascal_or_camel_cased_string] retournera une liste de caractères en minuscules séparés par des tirets bas. Les lettres majuscules sont précédées d'un tiret bas. C'est une méthode courante pour convertir des chaînes de caractères en snake_case.le if/else se trouve après la boucle for dans la liste de compréhension. Cela permet de conditionner la valeur à ajouter à la liste en fonction de la valeur actuelle de l'itérateur. Voici un exemple :
# numbers = [1, 2, 3, 4, 5]
# even_or_odd = ['even' if number % 2 == 0 else 'odd' for number in numbers]
def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case(input('Enter a Pascal or Camel cased string: ')))

    

main()