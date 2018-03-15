def code_bon(code):
    if code == 4242:
        print('Premier code bon.')
        return 1
    else:
        return 0
flag = 0
while True:
    print('Entrez le code :')
    n = int(input())
    if code_bon(n):
        flag = 1
    if flag == 1 and n == 2121:
        print('Bravo.')
        break