n = int(input())
taille = int(input())
s='Sorti de la ville'
for loop in range(taille):
    m = int(input())
    if m != n:
        s="Encore dans la ville"
        break
    else:
        s='Sorti de la ville'
print(s)

On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un certain nombre d'invités d'une fête.
 Écrivez un programme qui détermine combien d'invités ont été présents à un moment de la période étudiée.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de la période étudiée. 
L'entier suivant, nbInvites, est le nombre total d'invités. Pour chaque invité, votre programme doit ensuite 
lire deux entiers : sa date d'arrivée et de départ. Un invité est suspect si la période à laquelle il a été 
présent intersecte la période étudiée. Votre programme doit afficher le nombre d'invités suspects.


`