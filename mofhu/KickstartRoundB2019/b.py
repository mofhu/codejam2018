ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())

    d = {}
    stone = []
    t = set()

    for i in range(n):
        s, e, l = [int(t) for t in input().split(" ")]
        stone.append((s, e, l))
        if s not in t:
            t.add(s)
    # print(t)
    # print(stone)
    ans = 0
    for i in range(n):
        ti = i*stone[0][0]
        d[ti] = []
        for si in stone:
            eit = si[1] - ti * si[2]
            if eit < 0:
                eit = 0
            d[ti].append(eit)
    # print(d)

    used = []
    for i in range(n-1):
        ti = i*stone[0][0]
        ti1 = ti + stone[0][0]
        smax = -1
        jmax = -1
        for j in range(n):
            if j not in used:
                sj = d[ti][j] + sum(d[ti1]) - d[ti1][j]
                if sj >= smax:
                    smax = sj
                    jmax = j
                    # print(j, smax, jmax)
        ans += d[ti][jmax]
        used.append(jmax)
        # print(ans, used)

    # print(stone)
    for j in range(n):
        if j not in used:
            ans += d[(n-1)*stone[0][0]][j]

    print("Case #{}: {}".format(case, ans))


