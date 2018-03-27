s = input().upper()
new_s = ''
l = set()
for i in s:
    if i.isalpha():
        new_s += i
for i in [chr(x) for x in range(65, 92)]:
    print(new_s.count(i) / len(new_s))