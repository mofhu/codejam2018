# author: mofhu@github
# E. Add Modulo 10

t = int(input())

# import re
d = {}
for i in range(20):
    ii = i
    while ii < 20 and ii % 10 != 0:
        ii += ii % 10
    d[i] = ii

d = {
    0: 0, 1: 22, 2: 22, 3: 26, 4: 22, 5: 10,
    6: 26, 7: 26, 8: 22, 9: 26, 10: 10, 11: 26,
    12: 26, 13: 22, 14: 26, 15: 0, 16: 22, 17: 22, 18: 26, 19: 22}

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    amin = a[0]
    amax = a[0]
    ans = 'YES'
    s = d[a[0] % 20]
    for i in range(1,n):
        if amin > a[i]:
            amin = a[i]
        if amax < a[i]:
            amax = a[i]
        si = d[a[i] % 20]
        if si != s:
            ans = 'NO'
            print(ans)
            break
    else:
        if s == 0:
            if amax - amin == 5 or amax == amin:  # 15, 20
                ans = 'YES'
            else:
                ans = 'NO'
        elif s == 10:
            if amax - amin == 5 or amax == amin:  # 5, 10
                ans = 'YES'
            else:
                ans = 'NO'
        print(ans)

