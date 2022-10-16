# author: mofhu@github
# E. Scuza

t = int(input())
from bisect import bisect_right

for ncase in range(1, t+1):
    n, q = [int(s) for s in input().split(' ')]
    nn = [int(s) for s in input().split(' ')]
    qq = [int(s) for s in input().split(' ')]

    d = {0:0, nn[0]:nn[0]}
    dmax = nn[0]
    for i in range(1, n):
        if nn[i] > dmax:
            d[nn[i]] = d[dmax] + nn[i]
            dmax = nn[i]
        else:
            d[dmax] += nn[i]
    # print(d)  #
    key = sorted(d.keys())
    # print(key)

    ans = []
    for i in range(q):
        k = bisect_right(key, qq[i])
        # print(k)
        # print(key[k]-1)
        ans.append(str(d[key[k-1]]))

    print(' '.join(ans))



