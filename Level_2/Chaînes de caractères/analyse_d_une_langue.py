l = input()
n = int(input())
cnt = 0
for loop in range(n):
    line = input()
    for word in line: 
        for letter in word:
            if letter == l: cnt += 1
print(cnt)