n = int(input())
titres = [""] * n
for i in range(n):
    titres[i] = input()
titres.sort()
for i in range(n):
    print(titres[i])