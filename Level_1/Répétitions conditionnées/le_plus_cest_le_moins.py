n = int(input())
a = int(input())
cnt=0
while n!=a:
      if a<n:
         print("c'est plus")
      else:
         print("c'est moins")
      cnt+=1
      a = int(input())
print("Nombre d'essais nécessaires :\n" + str(cnt+1))
