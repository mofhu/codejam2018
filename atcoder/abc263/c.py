# author: mofhu@github
# C - Monotonically Increasing

n, m = [int(s) for s in input().split(' ')]

from collections import deque
q = deque()
i = 1
while i <= m-n+1:
    q.appendleft([i])
    i += 1
while len(q) > 0:
    t = q.pop()
    # print(t)
    if len(t) == n:
        print(' '.join([str(s) for s in t]))
    else:
        for j in range(m, t[-1], -1):
            q.append(t+[j])
