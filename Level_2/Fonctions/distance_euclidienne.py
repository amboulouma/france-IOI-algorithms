from math import *

def distance(a, b, x, y):
    return sqrt((x-a)**2 + (y-b)**2)


a, b, x, y = float(input()), float(input()), float(input()), float(input())
print(distance(a, b, x, y))


