ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())

    i = 0
    digit = 1
    pairs = {}
    while i <= n / 2:
        # print(i)

        def have4(j):
            j1 = str(j)
            for d in range(len(j1)-1,-1,-1):
                if j1[d] == '4':
                    j2 = j + 10*(len(j1)-1-d)
                    if j2 == j:
                        j2 += 1
                    return j2, len(j1)-d
            return False, 0

        def have4m(j):
            j1 = str(j)
            for d in range(len(j1)-1,-1,-1):
                if j1[d] == '4':
                    j2 = j - 10*(len(j1)-1-d)
                    if j2 == j:
                        j2 -= 1
                    return j2, len(j1)-d
            return False, 0

        t, d = have4(i)
        if not t:
            t1, d1 = have4m(n-i)
            if not t1:
                ans = " ".join([str(i), str(n-i)])
                break
            else:
                x = d1 - 1
                print(x, i, n-i)
                if x in pairs:
                    pairs[x].append((str(i)[-x:], str(n-i)[-x:]))
                elif x > 0:
                    pairs[x] = [(str(i)[-x:], str(n-i)[-x:])]
                i = n-t1
        else:
            i = t

    print(pairs)
    print("Case #{}: {}".format(case, ans))

    # print(d2)

