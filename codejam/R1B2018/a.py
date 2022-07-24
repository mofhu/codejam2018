ncase = int(input())
from math import floor

for case in range(1, ncase+1):
    n, l = [int(s) for s in input().split(" ")]
    ci = [int(s) for s in input().split(" ")]
    r = n - sum(ci)
    # print(n,l,r)
    # print(ci)
    per = {}
    res = {}
    for i in range(n):
        idn = i*100/n
        per[i] = floor(idn)
        if idn - per[i] >= 0.4999999995:
            per[i] += 1
            res[i] = 1
        else:
            res[i] = 0
    # print(per)
    # print(res)
    flag = False
    d1 = []
    for i in range(n-1):
        delta = res[i+1] - res[i]
        if delta == 1:
            flag = True
            d1.append(i)
    d1.sort()
    # print(d1)
    if len(d1) == 0:
        ans = 100
    else:
        # print(ci)
        ci += [0 for s in range(r)]
        ci.sort()
        # print(ci)
        mind = []
        for j in ci:
            for i in d1:
                if i >= j:
                    mind.append((i-j+1, j))
                    break
            else:
                mind.append((200000,j))
        mind.sort()
        # print(mind)
        j=0
        i = mind[j]
        ans = 0
        while r >= i[0]:
            r = r-i[0]
            ans += per[i[1] + i[0]]
            j += 1
            i = mind[j]
        # print(ans, r,j)
        if r > 0:
            ans += per[mind[j][1]+r]
            j+= 1
        # print(ans, r,j)
        for k in range(j, len(mind)):
            # print(k)
            # print(mind[k][1], per[mind[k][1]])
            ans += per[mind[k][1]]
            # print("ans", ans)


    print("Case #{}: {}".format(case, ans))

