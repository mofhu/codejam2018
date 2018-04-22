ncase = int(input())
# print(ncase)


for case in range(1, ncase+1):
    n,v1,h1,a,b,c,d,e,f,m = [int(s) for s in input().split(" ")]
    pos = []
    pos.append((v1,h1,0))
    for i in range(n-1):
        v = (a*v1 + b*h1 + c) % m
        h = (d*v1 + e*h1 + f) % m
        pos.append((v,h,i+1))
        v1 = v
        h1 = h
    # print(pos)
    ans = 0

    """
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                vi, hi = pos[i][0], pos[i][1]
                vj, hj = pos[j][0], pos[j][1]
                vk, hk = pos[k][0], pos[k][1]
                if vi == vj:
                    if vk == vj:
                        ans += 1
                        continue
                    elif abs(vk-vi) <= abs(hi-hj):
                        ans += 1
                        continue
                if vj == vk:
                    if vk ==vi:
                        ans += 1
                        continue
                    elif abs(vi-vj) <= abs(hj-hk):
                        ans += 1
                        continue
                if vk == vi:
                    if vk ==vj:
                        ans += 1
                        continue
                    elif abs(vj-vi) <= abs(hk-hi):
                        ans += 1
                        continue
                if hi == hj:
                    if hk ==hj:
                        ans += 1
                        continue
                    elif abs(hk-hi) <= abs(vi-vj):
                        ans += 1
                        continue
                if hj == hk:
                    if hi ==hj:
                        ans += 1
                        continue
                    elif abs(hi-hj) <= abs(vj-vk):
                        ans += 1
                        continue
                if hk == hi:
                    if hk ==hj:
                        ans += 1
                        continue
                    elif abs(hj-hi) <= abs(vk-vi):
                        ans += 1
                        continue
    """

    vpos = {}
    hpos = {}
    for v, h, r in pos:
        if h in hpos:
            hpos[h].append((v,h,r))
        else:
            hpos[h] = [(v,h,r)]
        if v in vpos:
            vpos[v].append((v,h,r))
        else:
            vpos[v] = [(v,h,r)]
    # print(vpos)
    # print(hpos)
    ranks = {}
    ans = 0
    for v in vpos:
        if len(vpos[v]) > 2:
            t = len(vpos[v])
            ans += int(t*(t-1)*(t-2) / 3 / 2)
            # print(ans)
        if len(vpos[v]) > 1:
            diffs = []
            for i in range(len(vpos[v])-1):
                for j in range(i+1,len(vpos[v])):
                    pi = vpos[v][i]
                    pj = vpos[v][j]
                    d = abs(pi[1] - pj[1])
                    diffs.append(d)
            diffs.sort()
            # print(diffs)
            for p in pos:
                if p[0] == v:
                    pass
                else:
                    d = abs(p[0] - v)
                    # print(diffs)
                    for i in range(len(diffs)):
                        if d < diffs[i]:
                            break
                    ans += i+1
    for h in hpos:
        if len(hpos[h]) > 2:
            t = len(hpos[h])
            ans += int(t*(t-1)*(t-2) / 3 / 2)
            # print(ans)
        if len(hpos[h]) > 1:
            diffs = []
            for i in range(len(hpos[h])-1):
                for j in range(i+1,len(hpos[h])):
                    pi = hpos[h][i]
                    pj = hpos[h][j]
                    d = abs(pi[0] - pj[0])
                    diffs.append(d)
            diffs.sort()
            # print(diffs)
            for p in pos:
                if p[1] == h:
                    pass
                else:
                    d = abs(p[1] - h)
                    # print(diffs)
                    for i in range(len(diffs)):
                        if d < diffs[i]:
                            break
                    ans += i+1
                    if i > 0:
                        for j in range(len(hpos[h])):
                            if p[0] == hpos[h][j][0]:
                                ans -= 1
                                # need add one more judge here?




    print("Case #{}: {}".format(case, ans))

