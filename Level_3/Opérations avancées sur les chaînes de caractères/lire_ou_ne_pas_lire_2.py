nbLivres = int(input())
plusGrandTitre = ""
for loop in range(nbLivres):
   titreLivre = input()
   if titreLivre > plusGrandTitre:
      plusGrandTitre = titreLivre
      print(titreLivre)