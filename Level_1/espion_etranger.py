# On vous donne un 'intervalle' de temps pendant lequel on sait qun espion est arrivé, puis la 'date arrivée'
# dun certain 'nombre' de personnes. 

# # Déterminez combien de ces personnes peuvent être cet espion.

# 'lire deux entiers' : 
#     la date de début 
#     la date de fin 
#     de intervalle 
#     pendant lequel on sait que espion est arrivé en ville.

# Il doit ensuite 'lire' 
#     un 'entier' nbEntrées, 
#     le 'nombre' total de personnes entrées dans la ville, 
#     puis les 'nbEntrées nombres' suivants qui représentent les dates entrée (non triées) des différentes personnes

# Votre programme doit 'afficher le nombre de personnes' entrées' entre les deux dates données, incluses'.


date_debut = int(input())
date_fin = int(input())
nb_entrees = int(input())
cpt = 0
for i in range(nb_entrees):
    dates_entrees = int(input())
    if dates_entrees <= date_fin and dates_entrees >= date_debut:
        cpt += 1 
print(cpt)