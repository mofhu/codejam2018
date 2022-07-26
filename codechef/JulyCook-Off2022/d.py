# author: mofhu@github
# K-MEX

t = int(input())
for n_case in range(t):
    n, m, k = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]

    # find mex == k -> contains 0,1,2,...,k-1 and any i>k
    # if m < k-1, not possible
    # else find all numbers -> yes
    # find enough other numbers (not k)
    ans = 'NO'
    if m <= k - 1:
        ans = 'NO'
    else:
        for i in range(k):
            if i not in a:
                ans = 'NO'
                break
        else:
            n_notk = 0
            for ai in a:
                if ai != k:
                    n_notk += 1
            if n_notk >= m:
                ans = 'YES'
    print(ans)
