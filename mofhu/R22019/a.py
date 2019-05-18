ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    m = []
    for i in range(n):
        x, y = (int(s) for s in input().split(" "))
        m.append((x,y))
    # print(m)
    m.sort(key=lambda x:x[1])
    m.sort(key=lambda x:x[0])
    # print(m)
    thresholds = []
    for i in range(n):
        for j in range(i+1,n):
            if m[i][1] > m[j][1]:  # [i][0] will always <= [j][0] by sort
                if m[i][0] < m[j][0]:
                    thresholds.append(((m[i][1] - m[j][1]), (m[j][0] - m[i][0])))
    # print(thresholds)
    thresholds.sort(key=lambda x:x[1])
    thresholds.sort(key=lambda x:x[0])
    # print(thresholds)
    t = len(thresholds)
    d = []
    for i in range(t):
        for j in range(i+1,t):
            x = thresholds[i]
            y = thresholds[j]
            # print(x,y)
            if x[0] * y[1] == x[1] * y[0]:
                d.append(j)
    d.sort(key=lambda x:0-x)
    # print(d)
    d0 = []
    for i in d:
        if i not in d0:
            del thresholds[i]
        d0.append(i)
    # print(thresholds)
    t = len(thresholds)
    ans = t+1

    print("Case #{}: {}".format(case, ans))


