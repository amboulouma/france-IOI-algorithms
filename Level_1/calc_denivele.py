# Votre programme 'lir'a dabord un entier représentant le nombre de montées
# et descentes que vous avez réalisées. 
# Pour chaque montée ou descente,

# il faut ensuite 'lir'e un entier représentant la variation daltitude, 
# cet entier étant strictement positif dans le cas dune montée et strictement 
# négatif dans le cas dune descente (il ny a rien à compter pour les tronçons 
# qui sont bien à plat). Votre programme devra afficher laltitude totale montée puis 
# laltitude totale descendue (ces deux nombres sont positifs).


n = int(input())
c1=0
c2=0
for loop in range(n):
    v = int(input())
    if v> 0 :
        c1 += v
    else:
        c2 += v
print(c1)
print(abs(c2))