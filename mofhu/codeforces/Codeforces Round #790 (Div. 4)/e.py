# author: mofhu@github
# E. Eating Queries

ncase = int(input())
import bisect
for case in range(1, ncase+1):
    n, q = [int(i) for i in input().split(' ')]
    s = [int(i) for i in input().split(' ')]
    s.sort(reverse=True)
    m = 0
    d = []
    for i in range(n):
        m += s[i]
        d.append(m)
    for i in range(q):
        t = int(input())
        if t > d[-1]:
            ans = -1
        else:
            ans = bisect.bisect_left(d, t)+1
        print(ans)
