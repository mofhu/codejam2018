# author: mofhu@github
# B. Luke is a foodie

t = int(input())

for ncase in range(1, t+1):
    n, x = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    ans = 0
    m0, m1 = a[0]-x, a[0]+x
    for i in range(1, n):
        if a[i]+x < m0 or a[i]-x > m1:
            ans += 1
            m0, m1 = a[i]-x, a[i]+x
        elif a[i]-x >m0:
            m0 = a[i]-x
        elif a[i]+x < m1:
            m1 = a[i]+x

    print(ans)
