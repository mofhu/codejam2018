# author: mofhu@github
# ASCII Art

ncase = int(input())
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for case in range(1, ncase+1):
    n = int(input())
    n -= 1
    d = {i:a[i] for i in range(26)}
    if n >= 26:
        s = n // 26
        # max n(n+1)/2 < s
        from math import sqrt, floor
        t = floor(sqrt(2*s))
        while t * (t+1) < 2*s:
            t += 1
        t -= 1
        if t < 2:
            t = 1
        res = n - t*(t+1) *13
        res = res % (int((t+1)*26))
        ans = d[res // (t+1)]
        # print('res t t(t+1)*26', res, t, t*(t+1)*13)
    else:
        ans = d[n]

    print("Case #{}: {}".format(case, ans))
