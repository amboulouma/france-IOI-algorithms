import sys
import math
# input = sys.stdin.readline
from datetime import time

print( list( map( str, range(10) ) ) )
print( list( map( float, range(10) ) ) )
print( list( map( chr, range(10) ) ) )

def listo(nbItems):
   for item in range(nbItems):
      if item % 7 == 0:
         return item % 10

print( list( map( listo, range(10) ) ) )
print(list(range(10)))
print(range(10))
print(map( str, range(10) ) )

nbItems = 10*1000
message = list( map( str, range(nbItems) ) )
print(time())
print(*message)
print(time())
