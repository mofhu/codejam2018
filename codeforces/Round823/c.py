# author: mofhu@github
# C. Minimum Notation

t = int(input())

from bisect import bisect_left

for ncase in range(1, t+1):
    s = [int(i) for i in input()]
    m = 9
    d = {i:[] for i in range(10)}
    for i in range(len(s)):
        d[s[i]].append(i)
        if s[i] < m:
            m = s[i]
    # print(m, d)
    maxi = d[m][-1]
    ans = str(m) * len(d[m])
    for i in range(m+1, 9):
        if len(d[i]) != 0:
            j = bisect_left(d[i], maxi)
            #t  print('d[i], j: ', d[i], j)
            # print(ans)
            ans += str(i) * (len(d[i]) - j)
            # print(ans)
            ans += str(i+1) * j
            # print(ans)
            if d[i][-1] > maxi:
                maxi = d[i][-1]
    if m != 9:
        ans += str(9) * len(d[9])


    print(ans)


