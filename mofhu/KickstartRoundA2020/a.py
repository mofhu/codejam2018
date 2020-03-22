ncase = int(input())


for case in range(1, ncase+1):
    n, b = (int(s) for s in input().split(' '))

    s = [int(s) for s in input().split(' ')]

    s.sort()
    # print(s)
    t = 0
    tsum = 0
    while t < n:
        if s[t] + tsum <= b:
            tsum += s[t]
            t += 1
        else:
            break
    # print(tsum)

    print("Case #{}: {}".format(case, t))

    # print(d2)

