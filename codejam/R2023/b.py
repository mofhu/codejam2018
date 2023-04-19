# author: mofhu@github
# Illumination Optimization

ncase = int(input())

for case in range(1, ncase+1):
    m, r, n = [int(i) for i in input().split(' ')]
    x = [int(i) for i in input().split(' ')]
    pos = 0
    i = 0
    ans = 0
    while pos < m:
        if i >= n or pos + r < x[i]:
            ans = 'IMPOSSIBLE'
            break
        else:
            while i < n and x[i] <= pos + r:
                i += 1
            ans += 1
            if i <= n:
                pos = x[i-1] + r
            else:
                if pos >= m:
                    break
                else:
                    ans = 'IMPOSSIBLE'
                    break

    print(f'Case #{case}: {ans}')
