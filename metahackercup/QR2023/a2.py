# author: mofhu@github
# A2: Cheeseburger Corollary 2

ncase = int(input())

from math import floor
for t in range(1, ncase + 1):
    a, b, c = [int(s) for s in input().split(' ')]
    # s: 2 bun 1 meat
    # d: 2 bun 2 meat
    # k: k+1 bun k meat
    if a > c and b > c:
        ans = 0
    else:
        ca = floor(c/a)
        cb = floor(c/b)
        # print(ca,cb)
        if ca > 2*cb:
            ans = ca
        elif cb >= ca:
            ans = 2*cb - 1
        else:
            ans = 2*floor((c-a)/b) + 1
    print('Case #{}: {}'.format(t, ans))
