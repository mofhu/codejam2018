# author: mofhu@github
# C. Most Similar Words

ncase = int(input())

for case in range(1, ncase+1):
    n, m = [int(i) for i in input().split(' ')]
    s = []
    ans = 9999999999
    for i in range(n):
        s.append(input())
    def diff(s1, s2):
        dist = 0
        d = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            d[alpha[i]] = i
        for i in range(m):
            dist += abs(d[s1[i]]-d[s2[i]])
        # print(s1, s2, dist)
        return dist
    for i in range(n):
        if ans == 0:
            break
        for j in range(i+1,n):
            d = diff(s[i], s[j])
            if d < ans:
                ans = d
    print("{}".format(ans))

