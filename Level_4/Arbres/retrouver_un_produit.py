n = int(input())
# Liste des codes avec leurs pos - 1, i+1 est dans code_pos[i]
code_pos = list(map(int, input().split()))
r = int(input())
# Liste des codes recherchés
codes = list(map(int, input().split()))

containers = []

for i in range(n):
    if i + 1 not in code_pos:
        containers.add(code_pos[i])

for i in range(r):
    print()