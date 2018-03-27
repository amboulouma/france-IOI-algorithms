main1 = input()
main2 = input()
cnt = 0
flag = 0
for i in range(min(len(main1), len(main2))):
    if main1[i] == main2[i]:
        cnt += 1
    if main1[i] < main2[i]:
        print(1)
        flag =1
        break
    elif main1[i] > main2[i]:
        print(2)
        flag =1
        break
         
if not(flag):
    if len(main1) < len(main2):
        print(2)
    elif len(main1) > len(main2):  
        print(1)
    else :
        print('=')
print(cnt)