# author: mofhu@github
# C. Build Permutation

t = int(input())

d = [i*i for i in range(1000)]
from collections import deque

for ncase in range(1, t+1):
    n = int(input())
    ans = deque()
    t = n-1
    while t >= 0:
        i = 0
        while d[i] < t:
            i += 1
        m = d[i] - t
        ans.appendleft([t-j for j in range(m-m,t+1-m)])
        t = m-1
        # print(ans)
    s = []
    for i in ans:
        s += [str(j) for j in i]
    print(' '.join(s))


