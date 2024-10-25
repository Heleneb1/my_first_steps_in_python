# def merge_sort(array):
#     middle_point = len(array) // 2
#     left_part = array[:middle_point]# methode de slicing pour diviser la liste en deux parties et les stocker dans des variables distinctes.
#     right_part = array[middle_point:]#idem

# Fonction de tri utilisant l'algorithme de tri fusion (merge sort)
def merge_sort(array):
    # Cas de base : Si le tableau contient un seul élément ou est vide, il est déjà trié
    if len(array) <= 1:
        return
    
    # Calcul du point médian pour diviser le tableau en deux parties
    middle_point = len(array) // 2
    left_part = array[:middle_point]    # Partie gauche du tableau, jusqu'au point médian
    right_part = array[middle_point:]    # Partie droite du tableau, à partir du point médian

    # Appel récursif pour trier chaque moitié du tableau
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialisation des index pour parcourir les deux sous-tableaux et le tableau principal
    left_array_index = 0    # Index pour la partie gauche
    right_array_index = 0   # Index pour la partie droite
    sorted_index = 0        # Index pour réinsérer dans le tableau principal

    # Fusionner les éléments des sous-tableaux en triant
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Si l'élément dans la partie gauche est plus petit, on l'ajoute au tableau principal
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            # Sinon, on ajoute l'élément de la partie droite
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Ajouter les éléments restants de la partie gauche, s'il en reste
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # Ajouter les éléments restants de la partie droite, s'il en reste
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

# Code pour tester la fonction de tri fusion
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]  # Tableau d'exemple
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)  # Appel de la fonction pour trier le tableau
    print('Sorted array: ' + str(numbers))  # Affichage du tableau trié
