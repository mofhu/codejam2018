# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    u = int(input())
    s = {}
    z0 = {}
    for i in range(10000):
        qi, si = input().split(' ')
        if si[0] not in s:
            s[si[0]] = 1
        else:
            s[si[0]] += 1
        if len(z0) < 10:
            if si[-1] not in z0:
                z0[si[-1]] = 1
            else:
                z0[si[-1]] += 1
    t = [(s[i], i) for i in s]
    t.sort(key=lambda x:x[0], reverse=True)
    for i in z0:
        if i not in s:
            ans = [i]
    for i in t:
        ans.append(i[1])
    print("Case #{}: {}".format(case, ''.join(ans)))

