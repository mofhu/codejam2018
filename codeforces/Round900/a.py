# author: mofhu@github
# A. How Much Does Daytona Cost?

t = int(input())

for ncase in range(1, t+1):
    n, k = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    if k in a:
        print('YES')
    else:
        print('NO')




