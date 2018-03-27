def min2(a, b):
    if a<b: return a
    else: return b
r=1000
for i in range(10):
    r = min2(int(input()), r)
print(r)