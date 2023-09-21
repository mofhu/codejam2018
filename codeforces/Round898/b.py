# author: mofhu@github
# B. Good Kid

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    a.sort()

    ans = 1
    a[0] += 1
    for i in a:
        ans *= i

    print(ans)


