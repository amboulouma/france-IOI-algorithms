# Il existe 4 types d'arbres :

# le "Tinuviel" fait moins de 5 mètres de haut et ses feuilles sont composées de plus 
# de 8 folioles
# le "Calaelen" fait plus de 10 mètres de haut et ses feuilles sont composées 
# de plus 10 folioles
# le "Falarion" fait moins de 8 mètres de haut et ses feuilles sont composées 
# de moins de 5 folioles
# le "Dorthonion" fait plus de 12 mètres de haut et ses feuilles sont composées 
# de moins de 7 folioles

# Votre programme lira deux entiers, la hauteur et le nombre de folioles de 
# larbre, et affichera le nom de larbre correspondant.
# Toutes les inégalités sont à prendre au sens large, cest-à-dire que "moins"
# signifie "moins ou égal" ou et "plus" signifie "plus ou égal".


n = int(input())
m = int(input())

if n <= 5 and m >= 8 :
    print("Tinuviel")
    
if n >= 10 and m >= 10 :
    print("Calaelen")
    
if n <= 8 and m <= 5 :
    print("Falarion")
    
if n >= 12 and m <= 7 :
    print("Dorthonion")
