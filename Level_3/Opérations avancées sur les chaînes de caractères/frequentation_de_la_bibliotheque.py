s = 0
try:
    while True:
        entiers = input().split(' ')
        for i in entiers:
            s += int(i)
except:
    print(s)