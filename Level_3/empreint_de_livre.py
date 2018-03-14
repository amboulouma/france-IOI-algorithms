indice_livre_livrenbLivres_nbJours = split(str(input()), " ")

nbLivres = int(nbLivres_nbJours[0])
nbJours = int(nbLivres_nbJours[1])
flag = 0
for loop in range(nbJours):
    nbClients = int(input())
    for loop in range(emprint):
        indice_livre_livre = split(str(input()), " ")
        indice_livre = int(indice_livre_livre[0])
        duree = int(indice_livre_livre[1])
    if indice_livre < nbLivres and flag == 0 :
        print(1)
    else :
        if duree + 
        print(0)


2 4         nblivre = 2, nbjours = 4
2           emprint = 2
0 3     1
1 3     1
1           emprint = 1
0 3     0
1           emprint = 1
1 4     0   
2           emprint = 2
0 2     1
0 5     0

si un client emprunte un livre le jour iJour pendant une durée duree alors celui-ci ne sera de nouveau disponible 
quau jour iJour + duree. 
De plus, si plusieurs personnes demandent le même livre pendant une journée, seule la première a une chance dêtre satisfaite.

nbPersonnes = int(input())
cpt = 0
for loop in range(2*nbPersonnes):
    arrivee = int(input())
    if arrivee >= 0:
        cpt+=1
print(cpt)
