ncase = int(input())

from math import floor

for case in range(1, ncase+1):
    l, r = (int(s) for s in input().split(" "))
    n = 0
    while (l > n or r > n):
        print('cycle', n,l,r, l-r)
        input()
        # z = input()
        # nn = int((3*n*n-n)/2 - n) + 100
        if n > 10 and l == r and l > n*n and r > n*n:
            if n%2 == 0:
                l -= int((n*(3*n-2) / 4))
                r -= int((n*(3*n) / 4))
                n = 2*n
            elif n%2 ==1:
                l -= int(((n+1)*(3*n-2) / 4))
                r -= int((n+1)*(n+1) / 2)
                n = 2*n + 1
        elif l>r and n > 10 and n>l-r and l > r and l > n*n and r > n*n:
            if n%2 == 0:
                l -= int((n*(3*n-2) / 4))
                r -= int((n*(3*n) / 4))
                n = 2*n
            elif n%2 ==1:
                l -= int(((n+1)*(3*n-2) / 4))
                r -= int((n+1)*(n+1) / 2)
                n = 2*n + 1
        elif l >= r and l > n*n and r > n*n:
            # find max t
            t = 0
            if n > 5:
                t = min(int(floor(l/n) - 1), n)
                if (t-n)%2 == 1:
                    t -= 1
                if t > 2:
                    lnt = int((2*n+t) / 4)
                    rnt = int((2*n+t) / 4) - t
                    l -= lnt
                    r -= rnt
                    n += t
            #
            if t <= 2:
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
                    print(n, l, r, mx, delta)
                    if n > 1:
                        nn = int((3*n*n-n)/2 - n)
                        print('t n nn', t, n, nn)
                        if t > nn and mx > nn and mx > delta:
                            t -= nn
                            n = n*2 -1
                            delta += nn
                            mx -= delta
                            l = mx
                            break
                    if t>n and mx > delta:
                        if n > 2:
                            tn = min(int(floor(t/n)) - 2, n)
                            stn = int((n+n+tn)*(tn+1) / 2) # sum n to n+tn
                            if tn > 2 and mx > stn and mx > delta:
                                stn = int((n+n+tn)*(tn+1) / 2) # sum n to n+tn
                                t -= stn
                                delta += stn
                                n += tn
                                print(n, l, r)
                                mx -= delta
                                l = mx
                                break
                        else:
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


