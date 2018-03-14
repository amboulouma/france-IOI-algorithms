a, b, n = int(input()), int(input()), int(input())
counter = 0
for i in range(n):
      x, y = int(input()), int(input())
      if not(y<a) and not(x>b):
        counter += 1;
print(counter)