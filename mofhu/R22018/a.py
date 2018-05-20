ncase = int(input())

for case in range(1, ncase+1):
    c = int(input())
    ci = [int(s) for s in input().split(" ")]
    t = []
    if ci[0] == 0 or ci[-1] == 0:
        ans = "IMPOSSIBLE"
    else:
        fi = []
        for i in range(c):
            if ci[i] != 0:
                out = ci[i]
                fi += [i] * out
        # print(fi)
        ff = [abs(fi[i] - i) for i in range(c)]
        # print(ff)
        # print(max(ff))
        ans = 1 + max(ff)
        t0 = ["."] * c
        for j in range(ans):
            t.append(t0[:])
        # print(t)
        for i in range(c):
            # print(i, t)
            for j in range(abs(fi[i] - i)):
                if fi[i] - i > 0:
                    # print(i, j, i+j )
                    t[0+j][i+j] = "\\"
                    # print(t)
                elif fi[i] - i < 0:
                    t[0+j][i-j] = "/"
        # print(t)
    if ans != "IMPOSSIBLE":
        print("Case #{}: {}".format(case, ans))
        for i in range(ans):
            print("".join(t[i]))
    else:
        print("Case #{}: {}".format(case, ans))

