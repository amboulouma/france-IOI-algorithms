# Programmez votre robot pour qu'il mène le rocher tout en haut des 21 marches de la
# pyramide et redescende ensuite tout en bas. Par exemple, si la pyramide ne faisait 
# que deux marches de haut, votre robot devrait effectuer le trajet illustré ci-dessous : 


# 1   haut, droite,                               gauche, bas.
# 2   haut, droite, haut, droite,                 gauche, bas, gauche, bas.
# 3   haut, droite, haut, droite, haut, droite,   gauche, bas, gauche, bas, gauche, bas.

from robot import *

for i in range(21):
    haut()
    droite()
for i in range(21):
    gauche()
    bas()

