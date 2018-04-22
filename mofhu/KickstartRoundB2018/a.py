ncase = int(input())


for case in range(1, ncase+1):
    f, l = [int(s) for s in input().split(" ")]

    ans = 0
    for i in range(f, l+1):
        if "9" in str(i) or i%9 == 0:
            pass
        else:
            ans += 1

    print("Case #{}: {}".format(case, ans))

    # print(d2)

