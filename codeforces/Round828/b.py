# author: mofhu@github
# B. Even-Odd Increments

t = int(input())

for ncase in range(1, t+1):
    n, q = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    even = 0
    odd = 0
    ans = 0
    for i in range(n):
        ans += a[i]
        if a[i] % 2 == 0:
            even += 1
    odd = n - even
    # print(even, odd)

    for i in range(q):
        t, x = [int(s) for s in input().split(' ')]
        if t == 0:
            ans += even * x
            if x % 2 != 0:
                even = 0
                odd = n
        else:
            ans += odd * x
            if x % 2 != 0:
                odd = 0
                even = n
        print(ans)


