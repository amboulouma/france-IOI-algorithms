s = input().upper().split(' ')
s = "".join(s)
max = 0
for i in s:
    if max <= s.count(i):
        max = s.count(i)
        r = i
print(r)