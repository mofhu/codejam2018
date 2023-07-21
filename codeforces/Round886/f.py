# author: mofhu@github
# F. We Were Both Children

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    a.sort()
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    s = [0 for i in range(n+1)]
    for key in d:
        i = 1
        while i * key <= n:
            s[i*key] += d[key]
            i += 1

    ans = max(s)
    print(ans)



