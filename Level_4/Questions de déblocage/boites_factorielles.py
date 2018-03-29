def factoriel(n):
   return 1 if n < 2 else n*factoriel(n-1)
 
nbPoids = int(input())
 
nbBoites = 1
while factoriel(nbBoites+1) <= nbPoids:
   nbBoites += 1
print(nbBoites)
    
def decompose(nbPoids,nbBoites):
   if nbBoites > 0:
      nbBoitesCourant = nbPoids // factoriel(nbBoites)
      decompose( nbPoids % factoriel(nbBoites), nbBoites-1 )
      print(nbBoitesCourant,end=" ")
       
decompose(nbPoids,nbBoites)