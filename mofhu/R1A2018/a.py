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
    ans = "POSSIBLE"
    if ncookies % frac != 0:
        ans = "IMPOSSIBLE"
    else:
        ave = int(ncookies / frac)
        # init crow, ccol
        crow = deque()
        frow = deque()
        for i in range(1, r):
            if sum(nrows[:i]) == ave * (v+1):
                crow.append([i])
        # print(crow)
        while(len(crow) > 0):
            st = crow.popleft()
            # print(st)
            if len(st) == h:
                frow.append(st)
            else:
                for j in range(st[-1], r):
                    if sum(nrows[st[-1]:j]) == ave * (v+1):
                        crow.append(st+[j])
        # print("frow:", frow)
        if len(frow) == 0:
            ans = "IMPOSSIBLE"

        ccol = deque()
        fcol = deque()
        for i in range(1, c):
            if sum(ncols[:i]) == ave * (h+1):
                ccol.append([i])
        # print(crow)
        while(len(ccol) > 0):
            st = ccol.popleft()
            # print(st)
            if len(st) == h:
                fcol.append(st)
            else:
                for j in range(st[-1], c):
                    if sum(ncols[st[-1]:j]) == ave * (h+1):
                        ccol.append(st+[j])
        # print("fcol:", fcol)
        if len(fcol) == 0:
            ans = "IMPOSSIBLE"
        if ans == "POSSIBLE":
            ans = "IMPOSSIBLE"
            while(ans == "IMPOSSIBLE" and len(frow)>0 and len(fcol)>0):
                rcut = frow.popleft()
                ccut = fcol.popleft()
                # print(rcut, ccut)
                r0 = 0
                c0 = 0
                flag = True
                i = 0
                j = 0
                while i in range(len(rcut)):
                    if flag == False:
                        break
                    while j in range(len(ccut)):
                        ri = rcut[i]
                        ci = ccut[j]
                        ca = sum(s[(x,y)] for x in range(r0,ri) for y in range(c0, ci))
                        # print(ca, ave)
                        if ca != ave:
                            flag = False
                            break
                        else:
                            r0, c0 = ri, ci
                            # print(ca, ave)
                            # p rint(i, j)
                            i+= 1
                            j+= 1
                            # print(i,j)

                if flag == True:
                    ans = "POSSIBLE"
                    break

    # print(r,c,h,v)
    # for row in rows:
    #     print(row)
    # print(s)
    # print(ncookies)
    # break

    print("Case #{}: {}".format(case, ans))

