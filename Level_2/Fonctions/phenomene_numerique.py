def suite(t):
    if not(t%2): return t/2
    else: return t*3 + 1
t=int(input())
while t != 1 :
    t = suite(t)
    print(int(t), end=" ")