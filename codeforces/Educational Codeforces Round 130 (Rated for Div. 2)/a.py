# author: mofhu@github
# A. Parkway Walk

ncase = int(input())

for case in range(1, ncase+1):
    n, m = [int(i) for i in input().split(' ')]
    a = [int(s) for s in input().split(' ')]

    ans = 0
    for i in range(n):
        if m >= a[i]:
            m -= a[i]
        else:
            ans += a[i] - m
            m = 0
    print(f'{ans}')
