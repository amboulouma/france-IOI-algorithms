def containsNotKnown(nom):
    r = False
    for i in nom:
        if not (i.isalpha()) and not (i.isdigit()) and i != '_':
            r = True
    return r


n = int(input())
for loop in range(n):
    nom = input()
    if nom[0].isdigit():
        print('NO')
    elif containsNotKnown(nom):
        print('NO')
    else:
        print('YES')
