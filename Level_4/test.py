n = 8
tab1 = [0] * n
tab2 = [0] * n
j=0
for i in "2 3 4 5 6 7 8 9".split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    tab1[j] = int(i)
    tab2[j] = abs(int(i))
    j += 1 
    
min = tab1[tab2.index(min(tab2))]
print(min)