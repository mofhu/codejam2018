ncase = int(input())
from collections import deque

for case in range(1, ncase+1):
    n = int(input())
    links = [s for s in input().split(" ")]

    best = 0
    s_all = [str(s) for s in range(1, n+1)]
    d = deque()
    for i in range(1, n+1):
        d.append([str(i)])
    while len(d) > 0:
        s = d.pop()
        i = s[-1]
        ni = links[int(i) - 1]
        if ni != s[0]:
            if len(s) > 2 and ni == s[-2]:
                for j in s_all:
                    if j not in s:
                        d.append(s+[ni]+[j])
            elif ni in s:
                continue
            else:
                d.append(s+[ni])
        else:
            # output
            if best < len(s):
                best = len(s)
                print(len(s), ": ", s)
                print(d)
            if best is n:
                break






    print("Case #{}: {}".format(case, best))



