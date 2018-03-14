# Votre robot doit faire 108 fois le tour du chemin vert représenté ci-dessous, 
# en tournant dans le sens des aiguilles d'une montre.

# Le robot se trouve initialement en bas à gauche. Chaque case représente 1 km, 
# donc pour faire un tour, le robot doit se déplacer successivement de 13 km dans 
# chacune des 4 directions.

# from robot import *
# haut()
# bas()
# gauche()
# droite()


from robot import *

for loop in range(108) :
    for loop in range(13) :
        haut()
    for loop in range(13) :
        droite()
    for loop in range(13) : 
        bas()
    for loop in range(13) :    
        gauche()
