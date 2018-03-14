n = int(input())
tab = [0]*n
for i in range(n):
    tab[i] = int(input())
tab.sort()
for i in range(n//2):
    print("{} {}".format(tab[i], tab[n-i-1]))
