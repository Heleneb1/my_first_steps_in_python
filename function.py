def my_function ():
    print("Hello from a function")# pour sorrtir de la fonction on doit appeler la fonction
my_function()#appel de la fonction




def my_function_with_args(username, greeting):# fonction avec des arguments
    print(f"Hello, {username}, from a function! I wish you {greeting}")
my_function_with_args("Bouba", "a great year!")#appel de la fonction avec des arguments

def ma_fonction (ma_variable=5):#fonction avec des arguments par défaut
    print('ma variable est:', ma_variable)
ma_fonction(42)#ici on a changé la valeur de la variable
ma_fonction()#appel de la fonction sans argument

def my_new_function(*args):#fonction avec un nombre variable d'arguments
   print("Le premier élément de la liste est:", args[0])
   print("Tous les éléments de la liste sont:", args)
   print(type(args))#affiche le type de la variable args c'est un tuple donc on ne peut pas modifier les éléments
my_new_function(1, 2, 3)#appel de la fonction avec des arguments

def my_new_function(**kwargs):#fonction avec un nombre variable d'arguments nommés
    print("Le premier élément de la liste est:", kwargs["name"])
    print("Tous les éléments de la liste sont:", kwargs)
    print(type(kwargs))#affiche le type de la variable args c'est un dictionnaire donc on peut modifier les éléments comme un objet en javascript
my_new_function(name="Bouba", age=42)#appel de la fonction avec des arguments

def sum(a, b):
    return a + b#fonction qui retourne la somme de deux nombres
print(sum(5, 6))#appel de la fonction
print(type(sum(5, 6)))#affiche le type de la variable retournée
#on peut aussi stocker la valeur retournée dans une variable
# x = sum(5, 6)
# print(x)
# print(type(x))
# print(sum(5, 6) + 1)#on peut aussi utiliser la valeur retournée directement dans une expression
a=0
def function_1():
    a=1
    print("function_1, a=",a ) 

def function_2():
    a=2
    print("function_2, a=",a )
function_1()
function_2()
print("a=",a)