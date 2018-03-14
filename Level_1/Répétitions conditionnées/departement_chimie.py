n,x,y = int(input()), int(input()), int(input())
cnt=0
a = int(input())
while cnt<n and a>=x and a<=y:
    print("Rien à signaler")
    cnt += 1
    try:
        a = int(input())
    except EOFError:
        break 
if cnt<n:
    print("Alerte !!")
