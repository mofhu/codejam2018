# author: mofhu@github
# D. Divide and Equalize

t = int(input())

from math import sqrt
for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    d = {}
    for ai in a:
        for i in range(2,int(sqrt(ai)+10)):
            while ai % i == 0:
                ai = int(ai / i)
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
        # print(ai)
        if ai != 1:
            if ai not in d:
                d[ai] = 1
            else:
                d[ai] += 1

    # print(d)
    ans = 'YES'
    for i in d:
        if d[i] % n != 0:
            ans = 'NO'
            break

    print(ans)

