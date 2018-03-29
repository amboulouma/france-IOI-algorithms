import sys
nbLignes,nbColonnes = map( int, sys.stdin.readline().split() )
 
tailles = [[1-int(pixel) for pixel in sys.stdin.readline().split()] for _ in range(nbLignes)]
for lig in range(1,nbLignes):
   for col in range(1,nbColonnes):
      if tailles[lig][col] > 0:
         tailles[lig][col] = \
            min(tailles[lig-1][col], tailles[lig][col-1], tailles[lig-1][col-1]) + 1
print( max( map(max,tailles) ) )