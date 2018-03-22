nom1, nom2 = input().split(' ')
amour1, amour2 = 0, 0
for i in nom1:
    amour1 += ord(i) - 65
for i in nom2:
    amour2 += ord(i) - 65
while amour1 >= 10:
    s = 0
    for i in str(amour1):
        s += int(i)
    amour1 = s
print(amour1, end=" ")
while amour2 >= 10:
    s = 0
    for i in str(amour2):
        s += int(i)
    amour2 = s
print(amour2, end=" ")
