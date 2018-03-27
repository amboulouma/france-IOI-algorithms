for i in range(40):
    for j in range(40):
        if i%2 == 0:
            if j%2 == 0 :
                print("O", end = "")
            else:
                print("X", end = "")
        else:
            if j%2 == 0 :
                print("X", end = "")
            else:
                print("O", end = "")
    print()

for loop in range(20):
    for loop in range(20):
        print("OX", end = "")
    print()
    for loop in range(20):
        print("XO", end = "")
    print()