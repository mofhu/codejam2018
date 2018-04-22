ncase = int(input())
# print(ncase)


for case in range(1, ncase+1):
    n, k, p = [int(s) for s in input().split(" ")]
    # print(n,k,p)
    n0 = [-1 for s in range(n)]
    # print(n0)

    for line in range(k):
        # print(line)
        a, b, c = [int(s) for s in input().split(" ")]
        # print(a)
        a -= 1
        n0[a] = c
    # print(n0)
    pstr = "{0:b}".format(p-1)
    j = len(pstr) - 1
    for i in range(len(n0)-1, -1, -1):
        if n0[i] == -1:
            n0[i] = pstr[j]
            j -= 1
            if j == -1:
                break
    # print(n0)
    for i in range(len(n0)):
        if n0[i] == -1:
            n0[i] = 0
        n0[i] = str(n0[i])
    ans = "".join(n0)

    print("Case #{}: {}".format(case, ans))

    # print(d2)

