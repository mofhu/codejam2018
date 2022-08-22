# author: mofhu@github
# A. Crossmarket

t = int(input())

for ncase in range(1, t+1):
    n, m = [int(s) for s in input().split(' ')]
    if n == 1 and m == 1:
        ans = 0
    else:
        ans = 2* (min(n, m)) + max(n, m) - 2
    print(ans)
