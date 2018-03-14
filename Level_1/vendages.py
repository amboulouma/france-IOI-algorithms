Le robot est initialement tout à gauche, là où se trouve un grand tas de raisins. 
Il devra, 20 fois :

ramasser des raisins pour remplir la hotte de ramassage ;
se rendre à la charrette ;
déposer le contenu de la hotte ;
revenir au point de départ.

gauche()
droite()
ramasser()
deposer()


from robot import *

for loop in range(20) :
    ramasser()
    for loop in range(15) :
        gauche()
    deposer()
    for loop in range(15) :
        droite()