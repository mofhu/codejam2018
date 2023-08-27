# author: mofhu@github
# A - Potions

n, h, x = [int(i) for i in input().split(' ')]
p = [int(i) for i in input().split(' ')]

ans = 0
for i in range(0, n):
    if p[i] >= x-h:
        ans = i+1
        break
print(ans)
