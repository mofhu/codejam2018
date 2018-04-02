ncase = int(input())

def check(n):
    imax = max(n)
    # print(imax, sum(n))
    if (imax * 2 <= sum(n)):
        return True
    else:
        return False

def printd():
    print("d = {", )
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        print("{}: '{}',".format(i, s[i]))
    print("}", )

# printd()

d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
     8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
     15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V',
     22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

for case in range(1, ncase+1):
    MAX_GROUP = 26
    ngroup = int(input())
    n = [int(s) for s in input().split(" ")]
    ans = ""

    while(sum(n) > 0):
        n1 = n[:]
        imax = max(n)
        # print(imax)
        # print(n.index(imax))
        iindex = n.index(imax)
        ans += d[iindex]
        n1[iindex] -= 1
        if check(n1):  # one check
            n = n1
            ans += " "
        else:
            imax = max(n1)
            if imax== n1[iindex]:  # two same
                ans += d[iindex] + " "
                n1[iindex] -= 1
                n = n1
            else:
                iindex = n1.index(imax)
                ans += d[iindex] + " "
                n1[iindex] -= 1
                n = n1
        # print(n)


    print("Case #{}: {}".format(case, ans))

