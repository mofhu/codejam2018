# author: mofhu@github
# A. Another String Minimization Problem

n = int(input())

for ncase in range(1, n+1):
    n, m = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    for i in range(n):
        if a[i] > m+1-a[i]:
            a[i] = m+1-a[i]
    a.sort()
    ans = []
    for ai in a:
        if ai not in ans:
            ans.append(ai)
        else:
            if m+1-ai not in ans:
                ans.append(m+1-ai)
    s = []
    for i in range(1, m+1):
        if i in ans:
            s.append('A')
        else:
            s.append('B')


    print(''.join(s))
