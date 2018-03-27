print('Tout droit tu grimperas,')
print('La clé tu trouveras,')
print('Habile tu seras,')
print('Quand tu les porteras,')
print('Et avec le chef tu reviendras !')

# Labyrinth

from robot import *

haut()
bas()
gauche()
droite()

from robot import *

haut()
haut() 
haut()
droite()
droite()
bas()
bas()
gauche()

# Tour de Hanoi

from robot import *
deplacer(zoneSource, zoneDestination)

from robot import *
deplacer(1, 3)
deplacer(1, 2)
deplacer(3, 1)



from robot import *

deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)

deplacer(1, 2)
deplacer(3, 1)
deplacer(3, 2)
deplacer(1, 2)

deplacer(1, 3)
deplacer(2, 3)
deplacer(2, 1)
deplacer(3, 1)
deplacer(2, 3)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)

# Recette secrete

5 volumes d'huile, 4 volumes d'eau, et 3 volumes d'un ingrédient 
secret.
deux tonneaux non gradués de contenances 5 litres et 3 litres,

Remplir tonneau
Vider tonneau
Transférer tonneauSource -> tonneauDestination

remplir(tonneau)
vider(tonneau)
transferer(tonneauSource, tonneauDestination)

Écrivez un programme qui effectue une série de transvasements 
permettant d'obtenir exactement 4 litres d'eau dans le plus 
grand tonneau.


from robot import *

remplir(5)
transferer(5, 3)
vider(3)
transferer(5, 3)
remplir(5)
transferer(5, 3)

0 0
5 0
2 3
2 0
0 2
5 2
4 1
4 0

135

for loop in range(135):
    print("Je dois respecter le Grand Sorcier.")

Aller à gauche
Aller à droite
Ramasser le récipient
Déposer le récipient

gauche()
droite()
ramasser()
deposer()

from robot import *
gauche()
gauche()
print("Bonjour, laissez-moi vous aider\n")
ramasser()
for loop in range(32):
   droite()
deposer()


from robot import *

for loop in range(15):
    gauche()
    ramasser()
gauche()
deposer()
