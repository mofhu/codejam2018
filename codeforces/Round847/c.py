# author: mofhu@github
# C. Premutation

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s = []
    for i in range(n):
        s.append([int(i) for i in input().split(' ')])
    ans = []
    if s[0][0] == s[1][0]:
        ans.append(s[0][0])
    else:
        ans.append(s[2][0])
    for i in range(n):
        if s[i][0] != ans[0]:
            ans += s[i]
    print(' '.join([str(i) for i in ans]))


