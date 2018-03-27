n, m = int(input()), int(input())
tab = [0]*n
for i in range(n):
    tab[i] = int(input())
for i in range(m):
    pos1,pos2 = int(input()), int(input())
    tab[pos1],tab[pos2] = tab[pos2],tab[pos1]
for i in range(n):
    print("{}".format(tab[i]))

