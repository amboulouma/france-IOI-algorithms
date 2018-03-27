n = int(input())
for i in range(n):
    livre = input()
    l = livre.lower().split(' ')
    l = "".join(l)
    if l == l[::-1]:
        print(livre)
