#  'lit' 
#     un numéro de mois algoréen,

# 'affiche' 
#     le nombre de jours de celui-ci. 



# 4	31
# 5	31
# 6	31
# 10	31

# 7	30
# 8	30
# 9	30
# 1	30
# 2	30
# 3	30

# 11	29



n = int(input())
if n == 7 or n == 8 or n == 9 or n == 1 or n == 2 or n == 3 :
    print(30)
if n == 4 or n == 5 or n == 6 or n == 10 :
    print(31)
if n == 11:
    print(29)
