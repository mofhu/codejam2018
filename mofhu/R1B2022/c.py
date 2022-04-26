# author: mofhu@github
# ASeDatAb

ncase = int(input())

import random

for case in range(1, ncase+1):
    # n = int(input())
    ans = 4
    s = '1'*ans + '0'*(8-ans)
    print(s)
    ans = int(input())
    while ans != 0:
        x = []
        while len(x) < ans:
            t = random.randrange(8)
            if t not in x:
                x.append(t)
        s = ''
        for i in range(8):
            if i in x:
                s += '1'
            else:
                s += '0'
        print(s)
        ans = int(input())
