# author: mofhu@github
# C. Jumping on Tiles

t = int(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
d = {alphabet[i]: i+1 for i in range(26)}
d00 = {alphabet[i]: i for i in range(26)}

for ncase in range(1, t+1):
    s = [i for i in input()]
    # print(s)
    d0 = {c:[] for c in alphabet}
    for i in range(len(s)):
        d0[s[i]].append(i+1)
    # print(d0)
    if s[0] == s[-1]:  # same
        ans = d0[s[0]]
        cost = 0
    elif s[0] < s[-1]:
        ans = []
        # print('ds0', d[s[0]], d[s[-1]]+1)
        for i in range(d00[s[0]], d00[s[-1]]+1):
            ans += d0[alphabet[i]]
            # print(ans)
    else:  # s[0] > s[-1]
        ans = []
        for i in range(d00[s[-1]], d00[s[0]]+1):
            d0[alphabet[i]].reverse()
            ans += d0[alphabet[i]]
            # print(ans)
        ans.reverse()

    cost = abs(d[s[-1]] - d[s[0]])
    m = len(ans)
    print(cost, m)
    print(' '.join(str(i) for i in ans))



