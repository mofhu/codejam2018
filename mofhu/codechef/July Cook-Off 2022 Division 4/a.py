# author: mofhu@github
# Enough Space

t = int(input())
for i in range(t):
    n, x, y = [int(s) for s in input().split(' ')]
    if n >= x + 2*y:
        print('YES')
    else:
        print('NO')
