# copper = {
#     'species': 'guinea pig',
#     'age': 2,
    
# }
# print(copper['species'])# pour afficher la valeur de la clé 'species' dans le dictionnaire 'copper'
# copper['food']='hay'# pour ajouter une nouvelle clé 'food' avec la valeur 'hay' au dictionnaire 'copper'

# copper['food'] = 'hay'
# copper['species'] = 'Cavia porcellus'
# del copper['age'] # Supprimer la clé 'age' du dictionnaire 'copper'

# for i, j in copper.items(): # Parcourir le dictionnaire 'copper' et afficher les clés et valeurs
#     print(i, j) # Afficher la clé et la valeur actuelles

#    targets_to_print =  [target] if target else graph # ternary operator

my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Initialisation de la liste des nœuds non visités
    unvisited = list(graph)
    
    # Initialisation des distances : distance de 'start' à lui-même est 0, les autres sont infinis
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Initialisation des chemins : chaque nœud a un chemin vide, sauf le point de départ
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Le chemin vers 'start' commence avec 'start'
    
    while unvisited:  # Tant qu'il y a des nœuds à explorer
        # Choisir le nœud non visité avec la plus petite distance actuelle
        current = min(unvisited, key=distances.get)
        
        # Pour chaque voisin du nœud actuel, on calcule la distance via 'current'
        for node, distance in graph[current]:
            # Si ce chemin vers 'node' est plus court, on met à jour la distance et le chemin
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                
                # Vérifie si le chemin actuel ne termine pas déjà avec 'node'
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]  # On copie le chemin du nœud courant
                else:
                    paths[node].extend(paths[current])  # On étend le chemin du nœud courant
                paths[node].append(node)  # On ajoute le nœud destination au chemin
        
        # Retire 'current' de la liste des nœuds non visités, il est maintenant traité
        unvisited.remove(current)
    
    # Si un nœud cible 'target' est spécifié, on prépare à afficher uniquement celui-ci
    targets_to_print = [target] if target else graph
    
    # Affiche les distances et chemins pour chaque nœud ciblé
    for node in targets_to_print:
        if node == start:  # Pas besoin d'afficher la distance du nœud vers lui-même
            continue
        print(f'\n{start}-{node} distance: {distances[node]}')  # Distance minimale
        print(f'Path: {" -> ".join(paths[node])}')  # Chemin suivi
    
    # Retourne le dictionnaire des distances et chemins pour référence éventuelle
    return distances, paths

# Exemple d'utilisation pour trouver le chemin le plus court de 'A' à 'F'
shortest_path(my_graph, 'A', 'F')

    