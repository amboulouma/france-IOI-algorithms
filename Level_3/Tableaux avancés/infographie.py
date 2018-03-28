# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

n, m = map(int, input().split())
tab = [["."] * m for _ in range(n)]
print(tab)
nr = int(input())
for i in range(nr):
    donneesRect = input().split()
    iLig1, iCol1, iLig2, iCol2 = map(int, donneesRect[:4])
    c = donneesRect[4]
    for i in range(iLig1, iLig2 + 1):
        for j in range(iCol1, iCol2 + 1):
            tab[i][j] = c
for ligne in tab:
      print("".join(ligne))
