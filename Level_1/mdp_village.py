# Votre programme lira un entier, l'heure d'arrivée, qui sera compris entre 0 et 12 inclus.
#  0 correspond à midi, 1 à 1h de l'après-midi, etc. et 12 à minuit.

# Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque heure après midi. 
# Il est donc de 15 pièces à 13h, etc. Il ne peut cependant pas dépasser 53 pièces.

# Votre programme devra afficher le prix à payer correspondant à l'heure d'arrivée donnée.

Votre programme doit lire un entier : le code fourni par 
lutilisateur. Si ce code correspond au code secret, qui est 64741, 
alors le programme devra afficher le texte « Bon festin ! ». 
Sinon, il devra afficher « Allez-vous en ! ».

nbMembres = int(input())

if nbMembres == 64741 :
    print("Bon festin !")
else:
    print("Allez-vous en !")




poids1=0
poids2=0

for loop in range(nbMembres):
    poids1 += int(input())
    poids2 += int(input())

if poids1 > poids2:
    print("L'équipe 1 a un avantage")
elif poids1 < poids2:
    print("L'équipe 2 a un avantage")

print("Poids total pour l'équipe 1 :", poids1)
print("Poids total pour l'équipe 2 :", poids2)


# if a+b>= 10 :
#     print('Taxe spéciale !')
#     print(36) 
# else:
#     print('Taxe régulière') 
#     print(2*(a+b))



# n = int(input())
# for loop in range(n):
#     poids = int(input())
#     age = int(input())
#     longueur = int(input())
#     hauteur = int(input())
#     print(longueur*hauteur + poids)

# print(1, 2, 3, 4, 5, sep = ",", end = " | ")


