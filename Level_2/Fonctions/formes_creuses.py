def ligne(n):
    for i in range(n):
        print('X', end='')
    print()
    print()


def rectangle(a,b):
    for i in range(a):
        for j in range(b):
            if i==0 or j==0 or i==a-1 or j==b-1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print()


def triangle(c):
    for i in range(c):
        for j in range(i+1):
            if j == 0 or j == i or i == c-1:
                print('@', end='')
            else:
                print(' ', end='')
        print()


n, a, b, c = int(input()), int(input()), int(input()), int(input())
ligne(n)
rectangle(a,b)
triangle(c)