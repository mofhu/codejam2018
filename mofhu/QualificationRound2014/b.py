ncase = int(input())

for n in range(1, ncase+1):
    c, f, x = [float(i) for i in input().split(" ")]
    # print(c, f, x)
    t0 = 0
    nf = 0
    while (1):
        t1 = t0 + x / (nf*f + 2)
        t2 = t0 + c / (nf*f + 2) + x / (nf*f + f + 2)
        if (t1 <= t2):
            print("Case #{}: {:.7f}".format(n, t1))
            break
        else:
            t0 += c / (nf*f + 2)
            nf += 1
