def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for problem in problems:
        first_number, operator, second_number = problem.split()

        # Validation des opérandes et de l'opérateur
        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calcul des résultats
        if operator == "+":
            result = int(first_number) + int(second_number)
        elif operator == "-":
            result = int(first_number) - int(second_number)

        # Formater les lignes pour l'affichage
        length = max(len(first_number), len(second_number)) + 2 # +2 pour l'espace et l'opérateur
        first_line += first_number.rjust(length) + '    '# rjust pour justifier à droite
        second_line += operator + second_number.rjust(length - 1) + '    '
        third_line += '-' * length + '    '
        fourth_line += str(result).rjust(length) + '    '

    # Retirer les espaces supplémentaires à la fin
    problems = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()#
    
    # Afficher les résultats si show_answers est True
    if show_answers:
        problems += '\n' + fourth_line.rstrip() # rstrip pour retirer les espaces à la fin

    return problems

# Test de la fonction
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')
