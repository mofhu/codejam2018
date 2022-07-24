ncase = int(input())
from math import gcd

for case in range(1, ncase+1):
    n = int(input())
    m = []
    for i in range(n):
        x, y = (int(s) for s in input().split(" "))
        m.append((x,y))
    # print(m)
    m.sort(key=lambda x:x[1])
    m.sort(key=lambda x:x[0])
    # print(m)
    thresholds = set()
    # max O(n2, n=300) -> len(thresholds) ~ 45000
    # use gcd to min(len(thresholds)) and ignore 2nd iteration
    for i in range(n):
        for j in range(i+1,n):
            if m[i][1] > m[j][1]:  # [i][0] will always <= [j][0] by sort
                if m[i][0] < m[j][0]:
                    x, y = m[i][1] - m[j][1], m[j][0] - m[i][0]
                    g = gcd(x,y)
                    x, y = int(round(x/g)), int(round(y/g))
                    if (x,y) not in thresholds:
                        thresholds.add((x,y))
    # print(thresholds)
    # print(thresholds)
    d = []
    # print(thresholds)
    t = len(thresholds)
    ans = t+1

    print("Case #{}: {}".format(case, ans))


