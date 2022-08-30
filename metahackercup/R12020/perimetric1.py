ncase = int(input())

for case in range(1, ncase + 1):
    n, k, w = [int(s) for s in input().split(' ')]
    l = [int(s) for s in input().split(' ')]
    al, bl, cl, dl = [int(s) for s in input().split(' ')]
    h = [int(s) for s in input().split(' ')]
    ah, bh, ch, dh = [int(s) for s in input().split(' ')]

    for i in range(k, n):
        l.append((al*l[i-2] + bl*l[i-1] + cl) % dl + 1)
        h.append((ah*h[i-2] + bh*h[i-1] + ch) % dh + 1)
    # print('w =', w)
    # print(l)
    # print(h)
    d = {}
    p = 0
    ans = 1
    for i in range(n):
        x0, y0 = l[i], h[i]
        if x0 not in d:
            p += 2*(w+h[i])  # no overlap
            for x in range(x0, x0+w+1):
                d[x] = h[i]
            # print(i,p,h[i],0, d)
        else:
            hmax = d[x0]
            # print('hmax', x0, d[x0])
            for x in range(x0, x0+w+1):
                if x in d and d[x] > hmax:
                    hmax = d[x]
                    # print('hmax', x, d[x])
                if x == x0 and h[i] > d[x]:
                    p += h[i] - d[x]
                    # print('++')
                    d[x] = h[i]
                elif x in d and h[i] > d[x]:
                    d[x] = h[i]
                elif x not in d:
                    p += 2
                    # print('+2')
                    d[x] = h[i]


            if hmax < h[i]:
                p += h[i] - hmax  # right end
                # print('+max')
            # print(i,p,h[i],hmax, d)
        ans = (ans * p) % 1000000007

    ans = ans % 1000000007
    print('Case #{}: {}'.format(case, ans))
