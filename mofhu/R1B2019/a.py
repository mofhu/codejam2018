ncase = int(input())

for case in range(1, ncase+1):
    p, q = [int(s) for s in input().split(' ')]
    sx = [0 for i in range(q+1)]  # len = q+1!
    sy = [0 for i in range(q+1)]
    se = []
    sw = []
    sn = []
    ss = []

    for j in range(p):
        x, y, d = [s for s in input().split(' ')]
        x = int(x)
        y = int(y)
        # print(x, y, d)  #
        # iterate x, y is too slow for large dataset in Python 3...
        if d is 'E':
            se.append(x)
        elif d is 'W':
            sw.append(x)
        elif d is 'N':
            sn.append(y)
        else:
            ss.append(y)
    se.sort()
    sw.sort()
    sn.sort()
    ss.sort()

    x = 0
    idx = 0
    for i in se:
        for j in range(idx+1, i+1):
            sx[j] += x
        idx = i
        x += 1
    for j in range(idx+1, q+1):
        sx[j] = x

    x = len(sw)
    idx = 0
    for i in sw:
        for j in range(idx, i):
            sx[j] += x
        idx = i
        x -= 1

    # print(sn)
    y = 0
    idy = 0
    # print('sy', sy)
    for i in sn:
        for j in range(idy+1, i+1):
            sy[j] += y
        idy = i
        y += 1
        # print(y,idy)
        # print('sy', sy)
    for j in range(idy+1, q+1):
        sy[j] = y

    # print(sx)
    y = len(ss)
    idy = 0
    for i in ss:
        for j in range(idy, i):
            sy[j] += y
        idy = i
        y -= 1

    x, y = 0, 0
    x = sx.index(max(sx))
    y = sy.index(max(sy))
    # print(sx)
    # print(sy)

    print("Case #{}: {} {}".format(case, x, y))


