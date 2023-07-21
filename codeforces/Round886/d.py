# author: mofhu@github
# D. Balanced Round

t = int(input())

for ncase in range(1, t+1):
    n, k = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    a.sort()

    longest = 1
    m = 1
    flag_new = 0
    for i in range(n-1):
        if a[i+1] - a[i] <= k:
            if flag_new == 0:
                m += 1
            else:
                m = 2
                flag_new = 0
        else:
            if flag_new == 0:
                if m > longest:
                    longest = m
            flag_new = 1
            m = 1
    else:
        if flag_new == 0:
            if m > longest:
                longest = m
    # print(m, longest)

    ans = n - longest

    print(ans)

