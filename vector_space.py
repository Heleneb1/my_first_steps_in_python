class R2Vector:
    def __init__(self, *, x, y):
        # Initialise les attributs x et y du vecteur
        self.x = x
        self.y = y

    def norm(self):
        # Calcule la norme (longueur) du vecteur en utilisant la formule racine carrée de (x^2 + y^2)
        return sum(val**2 for val in vars(self).values())**0.5

    def __str__(self):
        # Renvoie une représentation du vecteur sous forme de tuple (x, y) pour un affichage lisible
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        # Renvoie une représentation détaillée pour le débogage, du type R2Vector(x=..., y=...)
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        # Additionne deux vecteurs en additionnant leurs coordonnées respectives
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        # Soustrait deux vecteurs en soustrayant leurs coordonnées respectives
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        # Si other est un nombre, multiplie chaque coordonnée par ce nombre (produit scalaire)
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        # Si other est un vecteur, effectue le produit scalaire entre les deux vecteurs
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented

    def __eq__(self, other):
        # Vérifie l'égalité de deux vecteurs en comparant chaque coordonnée
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other):
        # Vérifie l'inégalité de deux vecteurs en inversant le résultat de __eq__
        return not self == other

    def __lt__(self, other):
        # Compare la norme de deux vecteurs pour déterminer si l'un est plus petit que l'autre
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        # Compare la norme de deux vecteurs pour déterminer si l'un est plus grand que l'autre
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        # Compare la norme pour vérifier si le vecteur est inférieur ou égal à un autre
        return not self > other

    def __ge__(self, other):
        # Compare la norme pour vérifier si le vecteur est supérieur ou égal à un autre
        return not self < other

class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        # Initialise les attributs x, y (avec super) et z pour un vecteur 3D
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        # Calcule le produit vectoriel entre deux vecteurs 3D
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)

# Exemples d'utilisation
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')
