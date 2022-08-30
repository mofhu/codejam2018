# author: mofhu@github
# A. Second Hands

ncase = int(input())

for t in range(1, ncase + 1):
    n, k = [int(s) for s in input().split(' ')]
    s = [int(s) for s in input().split(' ')]
    s.sort()
    d = {}
    ans = 'YES'
    for i in s:
        if i in d:
            if d[i] >= 2:
                ans = 'NO'
                break
            d[i] += 1
        else:
            d[i] = 1
    if 2 * k < n:
        ans = 'NO'
    print('Case #{}: {}'.format(t, ans))
