# author: mofhu@github
# B. 250 Thousand Tons of TNT

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s = [int(s) for s in input().split(' ')]
    ans = 0
    for i in range(1, max(3, int((n+2)/2))):
        if n % i == 0:
            imax = 0
            imin = 99999999999*150000
            for j in range(int(n / i)):
                nj = sum(s[i*j:i*j+i])
                # print(i, j, nj, imax, imin)
                if nj >= imax:
                    imax = nj
                if nj <= imin:
                    imin = nj
            ni = imax-imin
            if ni > ans:
                ans = ni
                # print(ans, imax, imin)
    print(ans)

