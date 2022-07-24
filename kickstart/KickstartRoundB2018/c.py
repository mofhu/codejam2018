ncase = int(input())
# print(ncase)

for case in range(1, ncase+1):
    n,v1,h1,a,b,c,d,e,f,m = [int(s) for s in input().split(" ")]
    pos = []
    pos.append((v1,h1,1))
    for i in range(n-1):
        v = (a*v1 + b*h1 + c) % m
        h = (d*v1 + e*h1 + f) % m
        pos.append((v,h,i+1))
        v1 = v
        h1 = h
    pos.sort()
    # print(pos)
    ans = 0
    dp = set()
    dn = set()
    d0 = set()
    snp0 = {}
    for i in range(n-1):
        sn = 0
        sp = 0
        s0 = 0
        for j in range(i+1, n):
            pi, pj = pos[i], pos[j]
            if pi[0] == pj[0] or pi[1] == pj[1]:
                d0.add((i,j))
                s0 += 1
            elif pi[1] < pj[1]:
                dp.add((i,j))
                sp += 1
            else:
                dn.add((i,j))
                sn += 1
        snp0[i] = [s0+sp+sn, s0+sn, s0+sp]
    # print(dp)
    # print(dn)
    # print(d0)
    # for i in snp0:
    #     print(i, snp0[i])

    for i, j in d0:
        # print(i, j)
        if j < n-1:
            ans += n-j-1
        # print(ans)
    for i, j in dp:
        # print(i, j)
        if j < n-1:
            ans += snp0[j][1]
        # print(ans)
    for i, j in dn:
        # print(i, j)
        if j < n-1:
            ans += snp0[j][2]
        # print(ans)

    print("Case #{}: {}".format(case, ans))

