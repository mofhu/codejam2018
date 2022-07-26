ncase = int(input())
from collections import deque

for case in range(1, ncase+1):
    r,c,h,v = [int(s) for s in input().split(" ")]

    rows = []
    s = {}
    ncookies = 0
    nrows = [0 for t in range(r)]
    ncols = [0 for t in range(c)]
    for i in range(r):
        row = input()
        rows.append(row)
        for j in range(len(row)):
            if row[j] == "@":
                ncookies += 1
                nrows[i] += 1
                ncols[j] += 1
                s[(i,j)] = 1
            else:
                s[(i,j)] = 0
    # print(nrows)
    # print(ncols)
    frac = (h+1)*(v+1)
    ans = "IMPOSSIBLE"
    if ncookies % frac != 0:
        ans = "IMPOSSIBLE"
    else:
        ave = int(ncookies / frac)
        # print(c)
        cut = deque()
        for i in range(1, r):
            for j in range(1, c):
                cut.append([(i,j)])
        # print(cut)
        while(ans == "IMPOSSIBLE" and len(cut) > 0):
            st = cut.popleft()
            flag = True
            # print("st", st)
            if len(st) == (h)*(v):  # finished cut
                # print("finished")
                r0, c0 = 0,0
                for i in range(len(st)):
                    ri, ci = st[i]
                    if i == 0:
                        ca = sum(s[(x,y)] for x in range(r0,ri) for y in range(c0, ci))
                        # print(ri, ci, ca)
                        if ca != ave:
                            flag = False
                            break
                        # else:
                        #     r0, c0 = ri, ci
                    if i == len(st) - 1:
                        ca = sum(s[(x,y)] for x in range(ri,r) for y in range(c0, ci))
                        # print("c1", ca)
                        if ca != ave:
                            flag = False
                            break
                        ca = sum(s[(x,y)] for x in range(r0,ri) for y in range(ci, c))
                        # print("c2", ca)
                        if ca != ave:
                            flag = False
                            break
                        ca = sum(s[(x,y)] for x in range(ri,r) for y in range(ci, c))
                        # print("c3", ca)
                        if ca != ave:
                            flag = False
                            break
                    if flag == False:
                        ans = "IMPOSSIBLE"
                    else:
                        # print("st finished", st)
                        ans = "POSSIBLE"
    # print(r,c,h,v)
    # for row in rows:
    #     print(row)
    # print(s)
    # print(ncookies)
    # break

    print("Case #{}: {}".format(case, ans))

