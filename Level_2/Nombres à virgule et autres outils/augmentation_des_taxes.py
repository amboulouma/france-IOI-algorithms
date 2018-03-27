
from math import *

taxe_fruits_legumes = float(input())
new_taxe_fruits_legumes = float(input())
prix_taxe_comprise = float(input())

prix = (prix_taxe_comprise/(taxe_fruits_legumes+100))*(100+new_taxe_fruits_legumes);

print(round(prix,2))