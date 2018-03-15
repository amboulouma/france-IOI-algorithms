n = int(input())
lmax = 0
for i in range(n):
    titre = input()
    if len(titre) > lmax :
        print(titre)
    lmax = max(lmax, len(titre))