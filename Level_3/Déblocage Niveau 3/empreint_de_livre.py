n, j = map(int, input().split())
tab_n = [0]*n
for jour in range(j):
    c = int(input())
    for loop in range(c):
        i, d = map(int, input().split())
        if tab_n[i] <= jour:
            print(1)
            tab_n[i] = jour+d
        else:
            print(0)