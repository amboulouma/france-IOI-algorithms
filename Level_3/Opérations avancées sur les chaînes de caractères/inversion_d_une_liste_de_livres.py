n = int(input())
titres = [""] * n
for i in range(n):
    titres[i] = input()
for i in range(n):
    print(titres[n-i-1])