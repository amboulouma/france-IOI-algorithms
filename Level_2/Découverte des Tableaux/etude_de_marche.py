n, m = int(input()), int(input())
tab = [0]*n
for i in range(m):
    tab[i] = int(input())
for i in range(n):
    cnt = 0
    for j in range(m):
        if tab[j] == i:
            cnt += 1
    print(cnt)