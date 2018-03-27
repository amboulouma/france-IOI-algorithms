

# On vous décrit une zone de recherche 'rectangulaire', parallèle aux axes, puis la 'position' dun certain nombre de maisons. 
# Écrivez un programme qui détermine combien de maisons sont dans cette zone.


# Il 'lira' ensuite le 'nombre' total de maisons, puis pour chaque 'maison', son 'abscisse' et son 'ordonnée'.

# Votre programme devra déterminer puis 'afficher' le 'nombre' de maisons qui se trouvent dans la 'zone' de recherche.
# Si une maison est exactement sur le 'bord de la zone, elle doit ête comptée.'

# Sur lexemple suivant
#     il y a 12 maisons, 
#     dont 5 sont dans la zone de recherche (en bleu) : 

# 1
# 4
# 1
# 8

# 12

# 1
# 7

# 1
# 9
# 2
# 3
# 3
# 2
# 3
# 4
# 3
# 6
# 3
# 9
# 5
# 3
# 5
# 8
# 7
# 5
# 8
# 2

# 8
# 8

# Out: 3

abscisse_minimale = int(input())
abscisse_maximale = int(input())
ordonnee_minimale = int(input())
ordonnee_maximale = int(input())

n_maison = int(input())

cpt = 0
for i in range(n_maison):
    x = int(input())
    y = int(input())
    if x>= abscisse_minimale and x<= abscisse_maximale and y>= ordonnee_minimale and y<= ordonnee_maximale:
        cpt += 1 
print(cpt)