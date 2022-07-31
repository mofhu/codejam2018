# author: mofhu@github
# To Divide or Not To Divide

t = int(input())
for ncase in range(t):
    a, b, n = [int(s) for s in input().split(' ')]
    if a % b == 0:
        ans = -1
    else:
        i = n - n % a
        while i < n or i % b == 0:
            i += a
        ans = i

    print(ans)
