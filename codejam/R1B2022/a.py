# author: mofhu@github
# Pancake Deque

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    d = [int(s) for s in input().split(' ')]
    i = 0
    j = n-1
    m0 = 0
    ans = 0
    while i <= j:
        if d[i] <= d[j]:
            if m0 <= d[i]:
                m0 = d[i]
                ans += 1
            i += 1
        else:
            if m0 <= d[j]:
                m0 = d[j]
                ans += 1
            j -= 1

    print(f'Case #{case}: {ans}')
