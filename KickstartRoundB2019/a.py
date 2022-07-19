ncase = int(input())

for case in range(1, ncase+1):
    n, q = [int(s) for s in input().split(" ")]
    s = list(input())
    # print(s)
    ans = 0
    for i in range(q):
        l, r = [int(t) for t in input().split(" ")]
        # print(l,r )
        if r == len(s):
            s1 = s[:][l-1:]
        else:
            s1 = s[:][l-1:r]
        # print(s1)
        d = {i:0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        # print(d)
        for j in s1:
            d[j] += 1
        flag = 0
        for j in d:
            if d[j] % 2 == 1:
                if flag == 1:
                    flag = -1
                    break
                else:
                    flag = 1
        if flag != -1:
            ans += 1
    print("Case #{}: {}".format(case, ans))


