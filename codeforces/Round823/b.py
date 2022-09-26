# author: mofhu@github
# B. Meeting on the Line

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    x = [int(s) for s in input().split(' ')]
    t = [int(s) for s in input().split(' ')]
    z = [(x[i], x[i]-t[i], x[i]+t[i]) for i in range(n)]
    ans = 0

    z.sort()
    # print(z)
    low = z[0][1]
    high = z[-1][2]
    for i in range(0, n):
        if z[i][1] < low:
            low = z[i][1]
        if z[i][2] > high:
            high = z[i][2]
    # print(low, high)
    ans = (low+high) / 2


    print(ans)


