n = int(input())
sum = 0
i=0
for i in range(n):
    if sum>n:
        break
    sum+=i*i;
if i > 0:
   i-=1;
   sum-=i*i;
else:
   i += 1
print(i-1)
print(sum)