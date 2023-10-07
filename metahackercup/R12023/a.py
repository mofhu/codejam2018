# author: mofhu@github
# A: Here Comes Santa Claus

ncase = int(input())

for t in range(1, ncase + 1):
    n = int(input())
    x = [int(s) for s in input().split(' ')]
    x.sort()
    if n != 5:
        l = (x[0]+x[1]) / 2
        r = (x[-1]+x[-2]) / 2
    else:
        l = (x[0]+x[1]) / 2
        r = (x[-1]+x[-2]) / 2
        if x[2] - l > r - x[2]:
            r = (x[2]+x[-1]) / 2
        else:
            l = (x[0]+x[2]) / 2
    ans = r-l
    print('Case #{}: {}'.format(t, ans))
