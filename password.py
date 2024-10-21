password = input("Enter your password: ")
if len(password) < 6:
    print("Password too short")
    if len(password) == 0:#l'indentation permet d'ajouter une condition à la condition précédente
        print("You did not enter a password")
elif password == "azerty":
    print("Access granted")
    print("Welcome to the system")
else:
    print("Bad password, Access denied")

print("End of program") 