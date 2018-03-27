n = int(input())
lmin = int(input())
for i in range(n):
    livre = input()
    resume = input()
    if len(resume) < lmin :
        print(livre)