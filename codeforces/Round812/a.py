# author: mofhu@github
# A. Traveling Salesman Problem

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    x = [0]
    y = [0]
    for i in range(n):
        xi, yi = [int(s) for s in input().split(' ')]
        x.append(xi)
        y.append(yi)

    ans = 2* (max(x)-min(x) + max(y)-min(y))
    print(ans)
