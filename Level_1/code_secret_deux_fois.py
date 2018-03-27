def entrez_code():
    cpt = 0
    while(True):
        nombreLu = float(input("Entrez le code :"))
        print()
        if nombreLu == 4242:
            if cpt == 1:
                print('Bravo.')
                break
            cpt += 1
            print('Encore une fois.')
            
entrez_code()

def attendreCode():
    tentative = 0
    while tentative != 4242:
        print("Entrez le code :")
        tentative = int(input())
        
attendreCode()
print("Encore une fois.")
attendreCode()
print("Bravo.")