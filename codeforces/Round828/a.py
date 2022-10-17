# author: mofhu@github
# A. Number Replacement

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    s = input()
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = s[i]
        else:
            if d[a[i]] != s[i]:
                ans = 'NO'
                break
    else:
        ans = 'YES'
    print(ans)




