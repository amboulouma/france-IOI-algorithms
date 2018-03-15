titre = input()
auteur = input()
tab = ['A','E','U','I','O', 'Y', ' ']
for i in titre:
    if i not in tab:
        print(i, end="")
print()
for i in auteur:
    if i not in tab:
        print(i, end="")