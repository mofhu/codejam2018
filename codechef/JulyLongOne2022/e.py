# author: mofhu@github
# Journey of the Knight

t = int(input())
for ncase in range(t):
    x1, y1, x2, y2 = [int(s) for s in input().split(' ')]
    if (x1+y1) % 2 == (x2+y2) % 2:
        print('YES')
    else:
        print('NO')
