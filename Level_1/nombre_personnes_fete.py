# Le premier entier à lire est 
#     nbPersonnes : le nombre total de personnes qui se sont rendues à la fête. 
    
# Ensuite, il y a 2 × nbPersonnes entiers à lire, 

# dans lordre chronologique des arrivées et départs. 

# Si lentier est positif, 
#     cest que la personne de numéro correspondant vient darriver,

# sil est négatif, 
#     elle vient de partir. 

# Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient là simultanément.



nbPersonnes = int(input())
cpt = 0
maxP = 0
for loop in range(2*nbPersonnes):
    arrivee = int(input())
    if arrivee >= 0 :
        cpt+=1
        if cpt > maxP:
            maxP = cpt
    else:
        cpt-=1
print(maxP)


# dfps = int(input())
# ddss = int(input())
# dfss = int(input())

# if ddss-dfps <= 0 and ddps-dfss <= 0 :
#     print('Amis')
# else: 
#     print('Pas amis')


# #     ddss <= ddps and dfss

# #     dfps = int(input())
# #     ddss = int(input())
# #     dfss = int(input())
    
    
# # bool = [ddps,dfps] inter [ddss, dfss]
# #      = [10,15] inter [1,5] = 0 pas amis
# #      = [3,6] inter [2,5] = [3, 5] amis
# #      = [4,6] inter [2,4] = {4} amis

