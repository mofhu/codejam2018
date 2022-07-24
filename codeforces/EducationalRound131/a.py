# author: mofhu@github
# A. Grass Field

n = int(input())

for ncase in range(1, n+1):
    a1 = [int(s) for s in input().split(' ')]
    a2 = [int(s) for s in input().split(' ')]
    t = sum(a1) + sum(a2)
    if t == 0:
        ans = 0
    elif t == 4:
        ans = 2
    else:
        ans = 1

    print(f'{ans}')
