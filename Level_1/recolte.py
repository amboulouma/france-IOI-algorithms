


maxN = int(input())
minN = int(input())

i = minN
s=0
for loop in range(maxN - minN + 1):
    s += i**2
    i+=1
print(s)

# 10 5 3
# Repeter nbVendeurs
#     afficher (positionDepart)
#     positionDepart = positionDepart + largeurEmplacement

print(1, 2, 3, 4, 5, sep = ",", end = " | ")