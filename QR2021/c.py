# author: mofhu@github
from math import floor

ncase = int(input())

for case in range(1, ncase+1):
    n, c = input().split(' ')
    n, c = int(n), int(c)
    if c < n - 1 or c > int(n*(n+1)/2) - 1:
        ans = 'IMPOSSIBLE'
    else:
        res = c - (n-1)
        idx = []  # where final pos of i in list
        i = 0
        while res > n - i -1 and i <= n-1:
            idx.append(n-i-1)
            res -= n - i-1
            i += 1
            # print(res, idx)
        else:
            if i <= n-1:
                idx.append(res)


        # print(idx)
        # 2341 -> 1432 -> 1234
        # 2431 -> 1342 -> 1243 -> 1234
        #


        ans = [str(i+1) for i in range(n)]
        flag = 0
        for i in range(len(idx)):
            t = floor(i/2)
            ans[t:idx[i]+1+t] = reversed(ans[t:idx[i]+1+t])
            # print(ans)
        ans = ' '.join(ans)

    print("Case #{}: {}".format(case, ans))

