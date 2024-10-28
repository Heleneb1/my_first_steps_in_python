class Category:
    def __init__(self, category):    
        self.category = category
        self.total = 0 
        self.initial = 0  # Correction de "inital"
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount
    
    def check_funds(self, amount):
        return amount <= self.total

    def withdraw(self, amount, description=""):         
        if self.check_funds(amount):             
            self.ledger.append({'amount': -amount, 'description': description})             
            self.total -= amount             
            return True         
        return False     

    def get_balance(self):         
        return self.total     

    def transfer(self, amount, category):         
        if self.check_funds(amount):             
            self.withdraw(amount, f"Transfer to {category.category}")             
            category.deposit(amount, f"Transfer from {self.category}")             
            return True         
        return False     

    def __str__(self):         
        title = f"{self.category:*^30}\n"         
        items = ""         
        for item in self.ledger:             
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'         
        total = f"Total: {self.total}"         
        return title + items + total                 

    def percentage_spent(self):            
        if self.initial == 0:  # Éviter la division par zéro
            return 0
        percentage = (self.total / self.initial) * 100     
        rounded_num = round(percentage, -1)      
        return rounded_num  

def create_spend_chart(categories):
    # Calculer le total des dépenses pour chaque catégorie
    withdrawals = []
    for category in categories:
        withdrawal = sum(item['amount'] * -1 for item in category.ledger if item['amount'] < 0)
        withdrawals.append(withdrawal)
    
    # Calculer le total de toutes les dépenses
    total = sum(withdrawals)
    
    # Calculer les pourcentages et les arrondir à la dizaine inférieure
    if total > 0:
        percentages = [int((amount / total * 100) // 10 * 10) for amount in withdrawals]
    else:
        percentages = [0 for _ in withdrawals]
    
    # Créer le graphique
    chart = "Percentage spent by category\n"
    
    # Ajouter les barres
    for i in range(100, -10, -10):
        chart += f"{str(i).rjust(3)}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Ajouter la ligne horizontale
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Ajouter les noms des catégories verticalement
    max_length = max(len(category.category) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i != max_length - 1:
            chart += "\n"
    
    return chart

# Test de la classe Category
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)