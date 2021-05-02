ncase = int(input())

for case in range(1, ncase+1):
    l, r = (int(s) for s in input().split(" "))
    n = 0
    while (l > n or r > n):
        nn = int((3*n*n-n)/2 - n) + 100
        if n > 100 and l == r and l > n*n and r > n*n:
            if n%2 == 0:
                l -= int((n*(3*n-2) / 4))
                r -= int((n*(3*n) / 4))
                n = 2*n
            elif n%2 ==1:
                l -= int(((n+1)*(3*n-2) / 4))
                r -= int((n+1)*(n+1) / 2)
                n = 2*n + 1
        elif l>r and n > 100 and n>l-r and l > r and l > n*n and r > n*n:
            if n%2 == 0:
                l -= int((n*(3*n-2) / 4))
                r -= int((n*(3*n) / 4))
                n = 2*n
            elif n%2 ==1:
                l -= int(((n+1)*(3*n-2) / 4))
                r -= int((n+1)*(n+1) / 2)
                n = 2*n + 1
        elif l >= r:
            mx = l
            mn = r
            t = mx - mn
            if t <= n:
                # here
                n += 1
                if t >= 1:
                    ntx = n*(t-1)
                    ntn = n*(t-1)
                l -= n
                continue
            delta = 0
            while (t>n and mx > delta):
                # print(n, l, r, mx, delta)
                if n > 1:
                    nn = int((3*n*n-n)/2 - n)
                    # print('t n nn', t, n, nn)
                    if t > nn and mx > nn and mx > delta:
                        t -= nn
                        n = n*2 -1
                        delta += nn
                if t>n and mx > delta:
                    n += 1
                    t -= n
                    delta += n
                    # print('n delta',n, delta)
            else:
                mx -= delta
                l = mx
        else:
            mx = r
            mn = l
            t = mx - mn
            # print(n,l,r,t)
            if t <= n:
                # here
                n += 1
                r -= n
                continue
            delta = 0
            while (t>n and mx > delta):
                # print(n, l, r, mx, delta)
                if n > 1:
                    nn = int((3*n*n-n)/2 - n)
                    # print('t n nn', t, n, nn)
                    if t > nn and mx > nn and mx > delta:
                        t -= nn
                        n = n*2 -1
                        delta += nn
                if t>n and mx > delta:
                    n += 1
                    t -= n
                    delta += n
                    # print('n delta',n, delta)
            else:
                mx -= delta
                r = mx

    ans = '{} {} {}'.format(n, l, r)

    print("Case #{}: {}".format(case, ans))


