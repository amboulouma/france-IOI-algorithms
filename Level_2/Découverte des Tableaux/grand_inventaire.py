n = int(input())
tab = [0 for i in range(10)]
for i in range(n):
    a,b = int(input()), int(input())
    tab[a-1] += b
for i in range(10):
    print(tab[i])
