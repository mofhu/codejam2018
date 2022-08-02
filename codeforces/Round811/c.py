# author: mofhu@github
# C. Minimum Varied Number

t = int(input())

for ncase in range(1, t+1):
    s = int(input())
    d = [i for i in range(9,-1,-1)]
    ans = []
    i = 0
    while s > d[i]:
        s -= d[i]
        ans.append(d[i])
        i += 1
    else:
        ans.append(s)
    ans.reverse()
    print(''.join([str(i) for i in ans]))

