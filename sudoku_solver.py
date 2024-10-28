class Board:
    def __init__(self, board):  # Initialisation de la classe avec un tableau de Sudoku.
        self.board = board  # Stocke le tableau initial dans l'attribut de l'instance.

    def __str__(self):  # Méthode spéciale pour l'affichage sous forme de chaîne de caractères.
        board_str = ''  # Chaîne qui contiendra le tableau formaté.
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]  # Remplace les zéros par des étoiles pour indiquer les cases vides.
            board_str += ' '.join(row_str)  # Convertit la ligne en chaîne de caractères séparée par des espaces.
            board_str += '\n'  # Ajoute un saut de ligne à la fin de chaque ligne du tableau.
        return board_str  # Retourne le tableau formaté.

    def find_empty_cell(self):  # Méthode pour trouver la prochaine case vide (contenant 0).
        for row, contents in enumerate(self.board):  # Parcourt chaque ligne avec son index.
            try:
                col = contents.index(0)  # Cherche l'index d'une case vide (0) dans la ligne actuelle.
                return row, col  # Retourne les coordonnées de la case vide trouvée.
            except ValueError:
                pass  # Si aucune case vide n'est trouvée dans la ligne, passe à la suivante.
        return None  # Retourne None si aucune case vide n'est trouvée.

    def valid_in_row(self, row, num):  # Vérifie si un nombre est déjà présent dans une ligne.
        return num not in self.board[row]  # Retourne True si le nombre n'est pas dans la ligne.

    def valid_in_col(self, col, num):  # Vérifie si un nombre est déjà présent dans une colonne.
        return all(self.board[row][col] != num for row in range(9))  # Retourne True si le nombre n'est pas dans la colonne.

    def valid_in_square(self, row, col, num):  # Vérifie si un nombre est déjà présent dans le carré 3x3.
        row_start = (row // 3) * 3  # Calcule le début de la sous-grille 3x3 en lignes.
        col_start = (col // 3) * 3  # Calcule le début de la sous-grille 3x3 en colonnes.
        for row_no in range(row_start, row_start + 3):  # Parcourt les lignes du carré.
            for col_no in range(col_start, col_start + 3):  # Parcourt les colonnes du carré.
                if self.board[row_no][col_no] == num:  # Si le nombre est déjà présent, retourne False.
                    return False
        return True  # Si le nombre n'est pas dans le carré, retourne True.

    def is_valid(self, empty, num):  # Vérifie si un nombre peut être placé à une position donnée.
        row, col = empty  # Décompose la position vide en coordonnées de ligne et colonne.
        valid_in_row = self.valid_in_row(row, num)  # Vérifie la validité dans la ligne.
        valid_in_col = self.valid_in_col(col, num)  # Vérifie la validité dans la colonne.
        valid_in_square = self.valid_in_square(row, col, num)  # Vérifie la validité dans le carré.
        return all([valid_in_row, valid_in_col, valid_in_square])  # Retourne True si toutes les vérifications sont valides.

    def solver(self):  # Algorithme de résolution du Sudoku.
        if (next_empty := self.find_empty_cell()) is None:  # Si aucune case vide n'est trouvée, le Sudoku est résolu.
            return True
        for guess in range(1, 10):  # Essaie chaque nombre possible de 1 à 9.
            if self.is_valid(next_empty, guess):  # Vérifie si le nombre peut être placé à la position vide.
                row, col = next_empty
                self.board[row][col] = guess  # Place le nombre dans la case.
                if self.solver():  # Appel récursif pour continuer la résolution.
                    return True
                self.board[row][col] = 0  # Réinitialise la case si le choix ne mène pas à une solution.
        return False  # Retourne False si aucune solution n'est trouvée avec les choix actuels.

def solve_sudoku(board):  # Fonction pour résoudre le Sudoku et afficher les résultats.
    gameboard = Board(board)  # Crée une instance de la classe Board avec le tableau de Sudoku donné.
    print(f'Puzzle to solve:\n{gameboard}')  # Affiche le puzzle à résoudre.
    if gameboard.solver():  # Lance la résolution.
        print(f'Solved puzzle:\n{gameboard}')  # Affiche le tableau résolu.
    else:
        print('The provided puzzle is unsolvable.')  # Affiche un message si le puzzle est insolvable.
    return gameboard  # Retourne l'objet Board.

# Exemple de puzzle de Sudoku à résoudre
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)  # Appel de la fonction pour résoudre le Sudoku.
