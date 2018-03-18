nbValeurs = int(input())
seuil = float(input())
valeurs = [float(input()) for loop in range(nbValeurs)]
temp = [0.0] * nbValeurs


def lisse():
    for valeur in range(1, nbValeurs):
        if abs(valeurs[valeur] - valeurs[valeur - 1]) > seuil:
            return False
    return True


nbTours = 0
while not lisse():
    nbTours = nbTours + 1
    for valeur in range(1, nbValeurs - 1):
        temp[valeur] = (valeurs[valeur - 1] + valeurs[valeur + 1]) / 2
    for valeur in range(1, nbValeurs - 1):
        valeurs[valeur] = temp[valeur]

print(nbTours)