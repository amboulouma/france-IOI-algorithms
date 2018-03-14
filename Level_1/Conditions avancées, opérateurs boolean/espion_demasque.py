t = int(input())
for i in range(t):
    counter = 0
    h,a,w,c,b = int(input()),int(input()),int(input()),int(input()),int(input())
    if h>=178 and h<=182:
        counter += 1
    if a>=34:
        counter += 1
    if w<70:
        counter += 1
    if not(c):
        counter += 1
    if b:
        counter += 1
    if counter == 5:
        print("Très probable")
    elif counter >= 3:
        print("Probable")
    elif counter == 0:
        print("Impossible")
    else:
        print("Peu probable")