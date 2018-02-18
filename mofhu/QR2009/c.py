# GCJ Qualification Round 2009 - C
# Author: Mo Frank Hu

n = int(input())
import re
from collections import deque

for ncase in range(1, n+1):
    w = "welcome to code jam"
    s = input()
    # init positions
    pos = []
    for i in range(len(w)):
        posi = []
        for j in range(len(s)):
            if s[j] is w[i]:
                posi.append(j)
        pos.append(posi)
    # print(pos)
    # construct strings
    ans = 0
    a = deque()
    for i in pos[0]:
        a.append((0, i))
    while(len(a) > 0):
        numc, endc = a.popleft()
        if numc is len(w)-1:  # finish string
            ans += 1
            if ans is 10000:
                ans = 0
            continue
        # very first version, no precise upper limit
        for i in pos[numc+1]:
            if i > endc:
                a.append((numc+1, i))
    if ans < 10:
        ans = "000" + str(ans)
    elif ans < 100:
        ans = "00" + str(ans)
    elif ans < 1000:
        ans = "0" + str(ans)
    else:
        ans = str(ans)
    
    print("Case #{}: {}".format(ncase, ans))