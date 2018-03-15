def pied(m):
    return m/0.3048


def gramme(g):
    return g*0.002205


def farhen(t):
    return 32 + 1.8*t


n = int(input())
for i in range(n):
    inputx = input().split(' ')
    a = float(inputx[0])
    t = inputx[1]
    if (t == 'm'):
        print(str(round(pied(a),6)) + " p")
    elif (t == 'g'):
        print(str(round(gramme(a),6)) + " l")
    elif (t == 'c'):
        print(str(round(farhen(a),6)) + " f")


