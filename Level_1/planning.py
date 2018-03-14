# Votre programme doit dabord lire un entier décrivant votre position actuelle sur la route, 
# sous la forme dun nombre de kilomètres par rapport au début de la route. Ensuite, il doit 
# lire un entier donnant le nombre de villages. Pour chaque village, il doit lire un entier
#  décrivant la position de ce village le long de cette même route. Votre programme doit
#   alors afficher le nombre de villages qui se trouvent à une distance inférieure ou égale 
#   à 50 km de votre position actuelle.

p = int(input())
v = int(input())
c=0
for loop in range(v):
    pr = int(input())
    if abs(pr-p) <= 50 :
        c += 1
print(c)