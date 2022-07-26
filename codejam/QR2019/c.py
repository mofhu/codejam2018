# author: mofhu@github
# Cryptopangrams

ncase = int(input())

N = 10000  # only works for small case
primes = [2]
for i in range(3, N+1):
    for j in primes:
        if i % j == 0:
            flag = True
            break
    else:
        primes.append(i)
# print(primes)
# print(len(primes))
def findp(i):  # find primes
    t = []
    for j in primes:
        if j <= i and j <= n+1 and i%j == 0:
            t.append(j)
            if i == j*j:  # wrong answer begins here: if two same letter occurs
                t.append(j)
                break
    return t

for case in range(1, ncase+1):
    n, l =[int(s) for s in input().split(" ")]
    p = [int(s) for s in input().split(" ")]
    pcase = []

    pprimes = []  # lists of two primes
    for i in p:
        pi = findp(i)
        pprimes.append(pi)
        if len(pcase) < 26:
            for j in pi:
                if j not in pcase:
                    pcase.append(j)
    pcase.sort()
    # print(pcase)
    # print(len(pcase))
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = {pcase[i] : t[i] for i in range(26)}

    print(pprimes)
    ans = []
    p0 = pprimes[0]
    p1 = pprimes[1]
    for p00 in p0:
        if p00 == p1[0] or p00 == p1[1]:
            if p00 == p0[0]:
                p01 = p0[1]
            else:
                p01 = p0[0]

    for i in pprimes:
        # print(i)
        # print(p01, s[p01])
        ans.append(s[p01])
        if i[0] != p01:
            p01 = i[0]
        else:
            p01 = i[1]
        # print(p01, s[p01])
    ans.append(s[p01])

    print("Case #{}: {}".format(case, "".join(ans)))

