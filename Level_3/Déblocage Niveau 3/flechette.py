nbLettres = int(input())
taille = 2 * nbLettres - 1
def trouveLettre(iLig, iCol):
   iLig = min(iLig, taille-1-iLig)
   iCol = min(iCol, taille-1-iCol)
   return chr( ord('a') + min(iLig, iCol) )
iLig = 0
for loop in range(taille):
   iCol = 0
   for loop in range(taille):
      print(trouveLettre(iLig, iCol), end = "")
      iCol = iCol + 1
   iLig = iLig + 1
   print("")