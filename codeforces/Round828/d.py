# author: mofhu@github
# D. Divisibility by 2^n

t = int(input())

from math import ceil

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    a2 = 0
    for i in a:
        t = i
        while t % 2 == 0:
            t /= 2
            a2 += 1
    ans = 0
    if n == 1:
        if a[0] % 2 == 0:
            ans = 0
        else:
            ans = -1
        print(ans)
        continue
    if a2 >= n:
        pass
    else:
        tlog = 1
        t = 2
        # generate best 2^i <= n?
        while t * 2 <= n:
            t *= 2
            tlog += 1
        nt = 1
        # print('n, a2, t, nt, tlog', n , a2, t, nt, tlog)
        t2n = 0
        while a2 + nt * tlog < n and t >= 2:
            # print('n, a2, t, nt, tlog', n , a2, t, nt, tlog)
            ans += nt
            a2 += nt * tlog
            t = int(t/2)
            tlog -= 1
            nt = int(n/t) - ans
        # print('n, a2, t, nt', n , a2, t, nt)
        if t <= 1:
            ans = -1
        else:
            # print('n, a2, t, ans', n, a2, t)
            nt = ceil((n - a2) / tlog )
            ans += nt
            # print('nt t ans', nt, t, ans)

    print(ans)




