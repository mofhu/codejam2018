ncase = int(input())

for case in range(1, ncase+1):
    d, n = [int(s) for s in input().split(" ")]
    t = 0

    for i in range(n):
        ki, si = [int(s) for s in input().split(" ")]
        ti = (d-ki) / si
        if ti > t:
            t = ti

    # print(t)


    print("Case #{}: {:.7f}".format(case, d/t))

