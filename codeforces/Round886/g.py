# author: mofhu@github
# G. The Morning Star

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    dx = {}
    dy = {}
    dxy = {}
    dx_y = {}
    d = [dx, dy, dxy, dx_y]
    for i in range(n):
        x, y = [int(i) for i in input().split(' ')]
        xy, x_y = x+y, x-y
        a = [x, y ,xy, x_y]
        for j in range(4):
            if a[j] not in d[j]:
                d[j][a[j]] = 1
            else:
                d[j][a[j]] += 1
    ans = 0
    for di in d:
        for key in di:
            if di[key] > 1:
                ans += di[key]*(di[key]-1)
    print(ans)






