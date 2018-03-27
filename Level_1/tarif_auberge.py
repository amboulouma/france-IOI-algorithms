# Une chambre ne coûte rien si on a 60 ans (lâge de laubergiste !) et 5 écus si 
# on a strictement moins de 10 ans. Pour les autres personnes cest 30 écus plus
# un supplément de 10 écus si on a au moins 20 kilos de bagages.

# Votre programme doit lire deux entiers, lâge et le poids des bagages de la personne 
# et doit afficher le prix, sous la forme dun entier.


n = int(input())
m = int(input())

if n == 60 :
    print(0)
    
elif n < 10 :
    print(5)
    
else:
    if m >= 20:
        print(40)
    else:
        print(30)
