# insert permet d'ajouter un élément à une liste à un index spécifique. La méthode prend deux arguments : l'index de l'élément à ajouter et l'élément lui-même. Voici un exemple :

# pop permet de supprimer un élément d'une liste à un index spécifique. La méthode prend un argument : l'index de l'élément à supprimer. Voici un exemple :
# Example Code
# fruits_list = ["cherry", "lemon", "tomato", "apple", "orange"]

# fruits_list.pop(2)

# lambda x: x + 1 une fonction lambda qui prend un argument x et renvoie x + 1. Les fonctions lambda sont des fonctions anonymes qui peuvent avoir n'importe quel nombre d'arguments mais ne peuvent contenir qu'une seule expression. Elles sont souvent utilisées pour des opérations simples et rapides.
# Example Code
# map(lambda x: x * 2, [1, 2, 3])

# test = lambda x: x * 2
# print(map(test,[2, 3, 5, 8]))
# You should see something like <map object at 0xd273a8> printed on the console, which is the string representation of the map object returned by map().

# To obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the list() function.

#print(list(map(test, [2, 3, 5, 8])))
#Titre : Expense Tracker
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()