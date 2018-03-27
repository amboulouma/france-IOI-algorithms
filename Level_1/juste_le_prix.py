# Vous arrivez dans un village le jour du marché, de nombreux marchands vendent 
# la spécialité locale, de délicieuses petites galettes. Elles ont toutes lair dêtre identiques,
#  donc vous décidez dacheter les moins chères.

# Votre programme doit lire un entier nbMarchands (non nul) puis les nbMarchands entiers suivants,
#  qui indiquent le prix des galettes chez chaque marchand, 
#  de la position 1  à la position nbMarchands. Votre programme devra ensuite afficher 
#  la position du plus petit de ces prix. En cas dégalité entre deux prix, 
#  on prendra la position la plus grande. Tous les prix et positions sont positifs 
#  et ne dépassent pas 1 million.







n = int(input())
pos = 1
posMin = 0
prix_min = 1000*1000
for loop in range(n):
    p = int(input())
    if prix_min >= p:
        prix_min = p
        posMin = pos
    pos += 1

print(posMin)

nbMarchands = int(input())
minPrix = 1000 * 1000
posMinPrix = -1
pos = 1
for loop in range(nbMarchands):
   prix = int(input())
   if prix <= minPrix:
      minPrix = prix
      posMinPrix = pos
   pos = pos + 1
print(posMinPrix)