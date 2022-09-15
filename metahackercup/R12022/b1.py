# author: mofhu@github
# B1: Watering Well - Chapter 1

ncase = int(input())

for t in range(1, ncase + 1):
    n = int(input())
    da = {}
    db = {}
    for i in range(n):
        a, b = [int(s) for s in input().split(' ')]
        if a not in da:
            da[a] = 1
        else:
            da[a] += 1
        if b not in db:
            db[b] = 1
        else:
            db[b] += 1
    q = int(input())
    dx = {}
    dy = {}
    for i in range(q):
        x, y = [int(s) for s in input().split(' ')]
        if x not in dx:
            dx[x] = 1
        else:
            dx[x] += 1
        if y not in dy:
            dy[y] = 1
        else:
            dy[y] += 1

    ans = 0
    for a in da:
        for x in dx:
            ans =  (ans + (abs(a-x) ** 2 * da[a] * dx[x])) % 1000000007
            # print(ans)
    for b in db:
        for y in dy:
            ans = (ans + abs(b-y) ** 2 * db[b] * dy[y]) % 1000000007
            # print(ans)
    print('Case #{}: {}'.format(t, ans))

