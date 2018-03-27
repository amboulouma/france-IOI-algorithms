n, m = map(int, input().split(' '))
tous_les_mots = []
longueurs = set()
longueurs_sorted = []
toutes_les_longueurs = []
for i in range(n):
    mots = input().split(' ')
    tous_les_mots.extend(mots)
for i in range(m*n):
    toutes_les_longueurs.append(len(tous_les_mots[i]))
for i in toutes_les_longueurs:
    longueurs.add(i)
for i in longueurs:
    longueurs_sorted.append(i)
longueurs_sorted.sort()
for i in longueurs_sorted:
    print("{} : {}".format(i, toutes_les_longueurs.count(i)))