# author: mofhu@github

ncase = int(input())
s = []

MAX = 1100000
for i in range(1, 10):
    t = i
    j = i
    si = str(i)
    while t < MAX:
        si = si + str(j+1)
        j += 1
        t = int(si)
        s.append(t)
for i in range(10, 100):
    t = i
    j = i
    si = str(i)
    while t < MAX:
        si = si + str(j+1)
        j += 1
        t = int(si)
        s.append(t)
for i in range(100, 1000):
    t = i
    j = i
    si = str(i)
    while t < MAX:
        si = si + str(j+1)
        j += 1
        t = int(si)
        s.append(t)
for i in range(1000, 10000):
    t = i
    j = i
    si = str(i)
    while t < MAX:
        si = si + str(j+1)
        j += 1
        t = int(si)
        s.append(t)
s = sorted(s)
# print(s[:100])
from bisect import bisect_right
for case in range(1, ncase+1):
    y = int(input())
    ans = s[bisect_right(s,y)]
    print("Case #{}: {}".format(case, ans))
# print(len(s))



