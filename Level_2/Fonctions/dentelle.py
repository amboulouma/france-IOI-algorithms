def ligneCaractere(caractere, longueur):
    for iCol in range(longueur):
        print(caractere, end = "")
    print()
l=int(input())
ligneCaractere('X',l)
ligneCaractere('#',l)
ligneCaractere('i',l)