ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(i) for i in input().split(' ')]
    s = [int(i) for i in input().split(' ')]
    ans = 0
    s = sorted(s)
    # print(s)
    # sd = [1] + s + [k]
    if len(s) == 1:
        t10, t11 = 0,0
        t2 = 0
    else:
        ds = [s[i+1] - s[i] for i in range(len(s)-1)]
        # print(ds)
        # delta max = delta -1 (use 2)
        # delta max side = delta (use 1)
        # delta max = delta/2 (use 1) odd
        # delta max = (delta-1)/2 (use 1) even
        # special 0,1 = 0
        # special 2 = 1 (same as 3)
        # print(side)
        sds = sorted(ds, reverse=True)
        # print(sds)
        from math import floor
        def ans1(num):
            if num <= 1:
                return 0
            else:
                return floor(num/2)
        def ans2(num):
            if num <= 1:
                return 0
            else:
                return num - 1
        t2 = ans2(sds[0])
        if len(s) == 2:
            t10, t11 = ans1(sds[0]), 0
        else:
            t10, t11 = ans1(sds[0]), ans1(sds[1])


    side = s[0] -1 , k-s[-1]
    # print(t2, t10, t11, side)
    t1 = sorted([t10, t11, side[0], side[1]], reverse=True)
    t1 = t1[0] + t1[1]
    ans = max(t2, t1)



    print("Case #{}: {:.6f}".format(case, ans/k))


