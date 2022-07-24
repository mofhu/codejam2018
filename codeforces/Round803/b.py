# author: mofhu@github
# Rising Sand

ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    if k == 1:
        if n % 2 == 0:
            ans = n // 2 - 1
        else:
            ans = (n-1) // 2
    else:
        ans = 0
        for i in range(1, len(a)-1):
            if a[i] > a[i-1] + a[i+1]:
                ans += 1
    print(ans)
