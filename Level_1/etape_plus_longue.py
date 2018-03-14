# Votre programme doit dabord 'lire' un entier strictement positif, le nombre de jours
# de marche effectués jusquà présent.

# Il doit ensuite 'lire', pour chaque jour, la distance parcourue ce jour-là. 

# Il doit alors afficher la distance maximale 
# parcourue en une journée.


v = int(input())
c=0
for loop in range(v):
    p = int(input())
    if c <= p :
        c = p
print(c)