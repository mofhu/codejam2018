# author: mofhu@github
# Controlled Inflation

ncase = int(input())

for case in range(1, ncase+1):
    n, p = input().split(' ')
    n, p = int(n), int(p)
    x = []
    xmm = []
    for i in range(n):
        x.append([int(s) for s in input().split(' ')])
        xmm.append([min(x[i]), max(x[i])])

    p0 = 0

    from collections import deque
    s = deque()
    s.append([0,0,0])
    ans00 = 0
    while(s):
        # print(xmm[i])
        i, p0, ans = s.popleft()
        # print(i, p0, ans)
        if i == n:
            if ans00 == 0 or ans < ans00:
                ans00 = ans
            continue
        pmin, pmax = xmm[i]
        if p0 <= pmin:
            ans += pmax - p0
            p0 = pmax
            s.append([i+1, p0, ans])
        elif p0 >= pmax:
            ans += p0 - pmin
            p0 = pmin
            s.append([i+1, p0, ans])
        else:

            ans0 = ans + pmax - p0 + pmax-pmin
            p00 = pmin
            s.append([i+1, p00, ans0])
            ans1 = ans + p0 - pmin + pmax-pmin
            p1 = pmax
            s.append([i+1, p1, ans1])


    print("Case #{}: {}".format(case, ans00))


