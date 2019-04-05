ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())

    for i in range(n):
        def have4(j):
            j = str(j)
            for s in j:
                if s == '4':
                    return True
            return False
        if not have4(i):
            if not have4(n-i):
                ans = " ".join([str(i), str(n-i)])
                break

    print("Case #{}: {}".format(case, ans))

    # print(d2)

