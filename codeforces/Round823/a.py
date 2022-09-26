# author: mofhu@github
# A. Planets

t = int(input())

for ncase in range(1, t+1):
    n, c = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    ans = 0
    for orbi in d:
        if d[orbi] >= c:
            ans += c
        else:
            ans += d[orbi]
    print(ans)


