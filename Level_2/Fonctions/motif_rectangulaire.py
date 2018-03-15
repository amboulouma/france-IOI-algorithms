def rectangleM(l, c, m):
    for i in range(l):
        for j in range(c):
            print(m, end = "")
        print()
l, c = int(input()), int(input())
m = input()
rectangleM(l, c, m)