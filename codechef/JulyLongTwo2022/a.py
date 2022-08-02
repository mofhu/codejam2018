# author: mofhu@github
# Insurance

t = int(input())
for ncase in range(t):
    x, y = [int(s) for s in input().split(' ')]
    if x >= y:
        print(y)
    else:
        print(x)
