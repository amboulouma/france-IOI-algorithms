


n = int(input())
for loop in range(n):
    poids = int(input())
    age = int(input())
    longueur = int(input())
    hauteur = int(input())
    print(longueur*hauteur + poids)

i = minN
s=0
for loop in range(maxN - minN + 1):
    s += i**2
    i+=1
print(s)

# 10 5 3
# Repeter nbVendeurs
#     afficher (positionDepart)
#     positionDepart = positionDepart + largeurEmplacement

print(1, 2, 3, 4, 5, sep = ",", end = " | ")



Votre programme doit d'abord lire le nombre de Karvas en 
compétition. Ensuite, pour chaque Karva, il doit :

lire 4 entiers : son poids, son âge, la longueur de ses cornes et 
la hauteur au garrot ;
afficher sa note, sachant qu'elle s'obtient en multipliant la 
longueur des cornes par la hauteur au garrot, valeur à laquelle on ajoute le poids.