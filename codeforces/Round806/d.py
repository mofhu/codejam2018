# author: mofhu@github
# D. Double Strings

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = {}
    d = {i:set() for i in range(1,9)}
    for i in range(n):
        s = input()
        if s not in a:
            a[s] = [i]
        else:
            a[s].append(i)
        d[len(s)].add(s)
    # print(d)
    # print(a)
    ans = ['0'] * n
    for s in a:
        for i in range(1, len(s)):
            j = len(s) - i
            ai = s[:i]
            aj = s[i:]
            # print(ai, aj)
            if ai in d[i] and aj in d[j]:
                idx = a[s]
                for ids in idx:
                    ans[ids] = '1'

    print(''.join(ans))
