# Le programme doit dabord 'lire' un entier strictement positif correspondant au nombre de maisons.
# Ensuite, pour chaque maison, il doit 'lire' la position horizontale (labscisse, le x) 
# et sa position verticale (lordonnée, le y) de cette maison. Toutes les abscisses
# et ordonnées sont des entiers compris entre zéro et 1 million.

# Le programme doit alors afficher le périmètre de la plus petite clôture rectangulaire 
# englobant toutes les maisons. Ce rectangle doit avoir ses côtés parallèles aux axes du repère,
# comme montré sur lillustration.

nbMaisons = int(input())
xMin = 1000 * 1000
xMax = 0
yMin = 1000 * 1000
yMax = 0
for loop in range(nbMaisons):
   posX = int(input())
   posY = int(input())
   if posX < xMin:
      xMin = posX
   if posX > xMax:
      xMax = posX
   if posY < yMin:
      yMin = posY     
   if posY > yMax:
      yMax = posY
      
largeur = xMax - xMin
hauteur = yMax - yMin
perimetre = 2 * (largeur + hauteur)
print(perimetre)