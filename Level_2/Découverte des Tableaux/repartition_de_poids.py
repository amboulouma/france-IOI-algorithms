n = int(input())
avg=0
tab = [0]*3000
for i in range(n):
    tab[i] = float(input())
for i in range(n):
    avg += tab[i]
avg/=n
for i in range(n):
    print(avg - tab[i])
        