nbMots = int(input())
couplesMots = [""] * nbMots
for idCouple in range(nbMots):
   premier, second = input().split(" ")
   couplesMots[idCouple] = second + " " + premier
couplesMots.sort()
for idCouple in range(nbMots):
   print(couplesMots[idCouple])