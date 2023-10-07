# author: mofhu@github
# C. Vasilije in Cacak

t = int(input())

for ncase in range(1, t+1):
    n, k, x = [int(s) for s in input().split(' ')]
    # min max by n, k
    xmin2 = k*(k+1)
    xmax2 = k*(n-k+1 + n)
    x2 = x*2
    if xmin2 <= x2 and x2 <= xmax2:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)


