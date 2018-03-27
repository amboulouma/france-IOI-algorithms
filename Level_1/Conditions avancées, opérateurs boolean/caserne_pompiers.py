
n_paires = int(input())
for loop in range(n_paires):

    abscisse_minimale1 = int(input())
    abscisse_maximale1 = int(input())
    ordonnee_minimale1 = int(input())
    ordonnee_maximale1 = int(input())

    abscisse_minimale2 = int(input())
    abscisse_maximale2 = int(input())
    ordonnee_minimale2 = int(input())
    ordonnee_maximale2 = int(input())

    if (abscisse_minimale1>=abscisse_maximale2 or abscisse_minimale2>=abscisse_maximale1 or ordonnee_minimale1>=ordonnee_maximale2 or ordonnee_minimale2>=ordonnee_maximale1) :
        print("NON")
    else:
        print("OUI")


