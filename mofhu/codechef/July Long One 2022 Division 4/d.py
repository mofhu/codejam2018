# author: mofhu@github
# Slow Solution

t = int(input())
for ncase in range(t):
    maxt, maxn, sumn = [int(s) for s in input().split(' ')]
    if sumn >= maxt * maxn:
        ans = maxt * maxn * maxn
    else:
        tn = sumn // maxn
        modn = sumn % maxn
        ans = tn * maxn * maxn + modn * modn
    print(ans)
