# On vous donne le nombre d'habitants d'un certain nombre de lieux que vous visitez. 
# Une ville étant un lieu dont la population est strictement supérieure à 10 000 habitants,
#  déterminez combien de lieux sont des villes.

# Votre programme doit lire un entier : le nombre de lieux. Il doit ensuite lire, 
# pour chaque lieu, un entier donnant le nombre de gens qui y habitent.
#  Votre programme doit alors afficher le nombre de villes.

n = int(input())
c=0
for loop in range(n):
    m = int(input())
    if m > 10000:
        c +=1
print(c)
