ncase = int(input())

for case in range(1, ncase+1):
    n, p = [int(s) for s in input().split(' ')]
    si = [int(s) for s in input().split(' ')]

    si.sort()
    # print(si)
    ans = 99999999999999999999
    for i in range(n-p+1):
        t = 0
        sub = si[i:i+p]
        m = sub[-1]
        for j in sub:
            t += m - j
        if t < ans:
            ans = t

    print("Case #{}: {}".format(case, ans))

    # print(d2)

