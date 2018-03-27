acronyme = input()
nbMots = len(acronyme)
nbLivres = int(input())
for _ in range(nbLivres):
   titre = [mot.capitalize() for mot in input().split()]
   if len(titre) == nbMots:
      correspondance = True
      for mot,initiale in zip(titre,acronyme):
         correspondance = correspondance and (initiale == mot[0])
      if correspondance:
         print(" ".join(titre))
