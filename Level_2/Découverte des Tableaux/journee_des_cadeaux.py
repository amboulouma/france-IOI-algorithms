n = int(input())
tab = [0]*n
for i in range(n):
    tab[i] = int(input())
tab.sort()
if n%2 == 0 :
    print(float(tab[n//2-1]+tab[n//2])/2)
else :
    print(tab[n//2])