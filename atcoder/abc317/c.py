# author: mofhu@github
# C - Remembering the Days

n, m = [int(s) for s in input().split(' ')]

r = {}
for i in range(n):
    for j in range(n):
        r[(i,j)] = 0

from collections import deque
s = deque()

for i in range(m):
    a, b, c = [int(s) for s in input().split(' ')]
    a = a-1
    b = b-1
    s.append(([a,b], c))
    r[(a,b)] = c
    r[(b,a)] = c


ans = 0
while len(s):
    t = s.pop()
    ti, length = t
    if length > ans:
        ans = length
    end = ti[-1]
    for i in range(n):
        if r[(end,i)] != 0 and i not in ti:
            s.append((ti+[i], length+r[(end,i)]))

print(ans)

