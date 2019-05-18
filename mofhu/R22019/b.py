ncase = int(input())
from math import gcd
from math import floor

for case in range(1, ncase+1):
    n = int(input())
    m = []
    for i in range(n):
        x, y = (int(s) for s in input().split(" "))
        m.append((x,y))
    # print(m)
    thresholds = []
    ans = ""
    flag = False
    for i in range(n):
        for j in range(i+1,n):
            if m[i][0] >= m[j][0] and m[i][1] >= m[j][1]:
                ans = "IMPOSSIBLE"
                flag = True
                break
            elif m[i][0] < m[j][0] and m[i][1] <= m[j][1]:
                pass
            elif m[i][0] <= m[j][0] and m[i][1] < m[j][1]:
                pass
            else:
                if m[i][0] < m[j][0] and m[i][1] > m[j][1]:
                    thresholds.append((m[i][0]-m[j][0], m[j][1]-m[i][1]))
                if m[i][0] > m[j][0] and m[i][1] < m[j][1]:
                    thresholds.append((m[i][0]-m[j][0], m[j][1]-m[i][1]))
        if flag == True:
            break

    print(thresholds)
    tp = []
    tn = []
    t = len(thresholds)
    if t == 0:
        ans = "1 1"
    else:
        for i in thresholds:
            if i[0] + i[1] > 0:
                tp.append(i)
            else:
                tn.append(i)
        d = []
        flag = thresholds[0][0] + thresholds[0][1]
        if flag > 0:
            flag = 1
        else:
            flag = -1
        t = len(tp)
        for i in range(tp):
            for j in range(i+1,t):
                x = tp[i]
                y = tp[j]
                # print(x,y)
                if x[0] * y[1] == x[1] * y[0]:
                    d.append(j)
        t = len(tn)
        for i in range(tn):
            for j in range(i+1,t):
                x = tn[i]
                y = tn[j]
                # print(x,y)
                if x[0] * y[1] == x[1] * y[0]:
                    d.append(j)
        if ans != "IMPOSSIBLE":
            d.sort(key=lambda x:0-x)
            # print(d)
            d0 = []
            for i in d:
                if i not in d0:
                    del thresholds[i]
                d0.append(i)
            # print(thresholds, flag)
            if flag == -1:
                thresholds.sort(key=lambda x:x[0]/x[1])
            else:
                thresholds.sort(key=lambda x:x[1]/x[0])
            x, y = abs(thresholds[0][0]), abs(thresholds[0][1])
            g = gcd(x, y)
            x, y = int(round(x / g, 0)), int(round(y / g,0))
            # print(g, x, y, flag)
            if flag == -1:
                if y%x == 0:
                    ans = "{} {}".format(y+1,x)
                else:
                    y0 = floor(y/x) + 1
                    ans = "{} {}".format(y0,1)
            else:
                if x%y == 0:
                    ans = "{} {}".format(1,x+1)
                else:
                    y0 = floor(x/y) + 1
                    ans = "{} {}".format(1,y0)

            # ans = t+1
            x, y = [int(s) for s in ans.split(" ")]
            print(x, y)
            for i,j in m:
                print(x*i + y*j)

    print("Case #{}: {}".format(case, ans))


