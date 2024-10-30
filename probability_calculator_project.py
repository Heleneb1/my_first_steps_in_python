import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents=[]
        for args in kwargs:
            for i in range(kwargs[args]):
                self.contents.append(args)
    def draw(self, num):
        if num >= len(self.contents):
        # Retourne toutes les boules 
            drawn_balls = self.contents[:]  # Utilise une copie pour éviter de modifier self.contents
            self.contents.clear()  # Vide le contenu si toutes les boules sont tirées
            return drawn_balls
        else:
            # Tire le nombre spécifié de boules
            drawn_balls = random.sample(self.contents, num)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls  # Retourne les boules tirées
 



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)

        # Crée un dictionnaire des quantités pour le tirage
        draw_counts = {color: balls.count(color) for color in expected_balls}

        # Vérifie si le tirage répond aux exigences
        meets_expectations = all(draw_counts.get(color, 0) >= count for color, count in expected_balls.items())
        
        if meets_expectations:
            success += 1

    return success / num_experiments  # En dehors de la boucle for


# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

 

