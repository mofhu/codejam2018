# author: mofhu@github
# Rainbow Sort

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = [i for i in input().split(' ')]
    s0 = set()
    ans = []
    t = 0
    flag = False
    for i in range(n):
        if s[i] in s0 and s[i] != t:
            ans = 'IMPOSSIBLE'
            flag = True
            break
        elif s[i] not in s0:
            s0.add(s[i])
            ans.append(s[i])
            t = s[i]
    if flag:
        print("Case #{}: {}".format(case, ans))
    else:
        print("Case #{}: {}".format(case, ' '.join(ans)))
