# author: mofhu@github
# D. Friends and the Restaurant

t = int(input())

# import re
for ncase in range(1, t+1):
    n = int(input())
    x = [int(s) for s in input().split(' ')]
    y = [int(s) for s in input().split(' ')]
    diff = [y[i] - x[i] for i in range(n)]
    diff.sort(reverse=True)
    # print(diff)
    ans = 0
    i = 0
    j = n-1
    while i < j:
        if diff[i] < 0:
            break
        elif diff[i] + diff[j] >= 0:
            i += 1
            j -= 1
            # print(diff[i], diff[j])
            ans += 1
        else:
            while diff[i] + diff[j] < 0 and i < j:
                j -= 1
            if diff[i] + diff[j] >= 0 and i < j:
                # print(diff[i], diff[j])
                i += 1
                j -= 1
                ans += 1
    print(ans)





