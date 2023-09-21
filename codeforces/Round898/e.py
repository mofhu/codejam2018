# author: mofhu@github
# E. Building an Aquarium

t = int(input())

for ncase in range(1, t+1):
    n, x = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    a.sort()
    s = []  # step
    for i in range(1, n):
        if a[i] > a[i-1]:
            s.append(i)
    # s.append(n)
    # print(s)

    i = 0
    h0 = a[i]
    s0 = 0  # sum

    for j in range(len(s)):
        h1 = a[s[j]]
        s1 = s0 + (h1-h0) * s[j]
        # print(f'h1 {h1}, s[j] {s[j]}, s1 {s1}')
        if s1 > x:
            break
        else:
            s0 = s1
            h0 = h1
    else:  # not big
        s = [n]
        j = 0
    # s1 overflow

    from math import floor
    ans = floor((x-s0) / s[j]) + h0
    print(ans)






