
def contientIntervalle(tabi, tabM, indice):
    c = 0
    for i in range(len(tabM)):
        if i == indice:
            continue
        if tabi[0] <= tabM[i][0] and tabi[1] >= tabM[i][1]:
            c += 1
    return c

nbManteaux = int(input())
tab = [[0, 0] for _ in range(nbManteaux)]
max = 0
for i in range(nbManteaux):
    tab[i][0], tab[i][1] = map(int, input().split())

for i in range(nbManteaux):
    if max < contientIntervalle(tab[i], tab, i):
        max = contientIntervalle(tab[i], tab, i)
print(max)