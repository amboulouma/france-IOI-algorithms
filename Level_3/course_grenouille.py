nbGrenouilles = int(input())
nbTours = int(input())
positions = [0] * (nbGrenouilles + 1)
nbToursEnTête = [0] * (nbGrenouilles + 1)
maximum = 0

for loop in range(nbTours - 1):
    grenouille, bond = map(int, input().split())
    positions[grenouille] = positions[grenouille] + bond
    if positions[grenouille] > maximum:
        nbToursEnTête[grenouille] = nbToursEnTête[grenouille] + 1
        maximum = positions[grenouille]
        grenouilleEnTête = grenouille
    elif positions[grenouille] == maximum:
        grenouilleEnTête = 0
    nbToursEnTête[grenouilleEnTête] = nbToursEnTête[grenouilleEnTête] + 1

nbToursEnTête[0] = 0
grenouilleGagnante = 1
nbToursGagnante = 0
for grenouille, nbTours in enumerate(nbToursEnTête):
    if nbToursGagnante < nbTours:
        nbToursGagnante = nbTours
        grenouilleGagnante = grenouille

print(grenouilleGagnante)