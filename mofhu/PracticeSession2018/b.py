ncase = int(input())

def check(n):
    imax = max(n)
    # print(imax, sum(n))
    if (imax * 2 <= sum(n)):
        return True
    else:
        return False


d = {0:"A", 1:"B", 2:"C",
     3:"D", 4:"E", 5:"F"}

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

