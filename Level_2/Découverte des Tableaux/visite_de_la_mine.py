n = int(input())
tab = [0]*3000
for i in range(n):
    tab[i] = int(input())
for i in range(n-1, -1, -1):
    if(tab[i]==5):
        print(4)
    elif(tab[i]==4):
        print(5)
    elif(tab[i]==2):
        print(1)
    elif(tab[i]==1):
        print(2)
    else:
        print(tab[i])
