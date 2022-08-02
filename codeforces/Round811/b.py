# author: mofhu@github
# B. Remove Prefix

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    ans = 0
    s = set()
    for i in range(n-1, -1, -1):
        if a[i] not in s:
            s.add(a[i])
        else:
            print(1+i)
            break
    else:
        print(0)


