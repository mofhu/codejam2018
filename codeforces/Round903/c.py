# author: mofhu@github
# C. Perfect Square

t = int(input())

s = 'abcdefghijklmnopqrstuvwxyz'
d = {s[i]: i for i in range(26)}
for ncase in range(1, t+1):
    ans = 0
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    # build list
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            # 01, 13, 32, 20
            # print(i, j)
            chars = s[i][j], s[j][n-1-i], s[n-1-i][n-1-j], s[n-1-j][i]
            dc = [d[k] for k in chars]
            for k in dc:
                ans += max(dc) - k
    # calz to max char
    # break
    print(ans)


