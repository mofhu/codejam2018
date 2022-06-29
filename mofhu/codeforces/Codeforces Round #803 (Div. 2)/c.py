# author: mofhu@github
# C. 3SUM Closure

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    ans = 'NO'
    if n == 3:
        if (a[0] + a[1] + a[2]) in a:
            ans = 'YES'
    elif n == 4:  # n > 3
        if a[0] + a[1] + a[2] in a and a[1] + a[2] + a[3] in a:
            if a[0] + a[1] + a[3] in a and a[0] + a[2] + a[3] in a:
                ans = 'YES'
    else:  # n > 4 must be long 0 string and end numbers
        a = sorted(a)
        # print(a)
        if a[1] == 0 and a[-2] == 0:
            if a[0] + a[-1] in a:
                ans = 'YES'
    print(ans)

