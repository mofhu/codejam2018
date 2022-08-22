# author: mofhu@github
# B. Beautiful Array

t = int(input())
from math import floor

for ncase in range(1, t+1):
    n, k, b, s = [int(s) for s in input().split(' ')]

    minb = floor((s-(k-1)*(n-1))/k)
    maxb = floor(s/k)
    # print('minmax', minb, maxb)
    if b < minb or b > maxb:
        ans = ['-1']
    else:
        ans = []
        if n == 1:
            ans = [str(s)]
        elif k == 1:
            ans += [str(0)] * (n-1) + [str(s)]
        else:
            if (n-1)*(k-1) < s-b*k:
                a0 = b*k + (s-b*k-(n-1)*(k-1))
                # print('a0', a0)
                ans.append(str(a0))
            else:
                a0 = b*k
                ans.append(str(a0))
            if k != 1:
                num_k_1 = floor((s - a0)/(k-1))
                ans += [str((k-1))] * num_k_1
                if num_k_1 != n-1:
                    ans += [str(0)] * (n-2-num_k_1)
                    ans.append(str((s-a0)%(k-1)))
                # a0 += (s-b*k)%(k-1)  #
    print(' '.join(ans))


