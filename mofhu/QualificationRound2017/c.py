x = int(input())

# import time

for case in range(1, x + 1):
    n, k = [int(s) for s in input().split(" ")]
    i = 0
    j = 0
    while (2**i <= k):
        i += 1
    while (2**j <= n):
        j += 1
    # print(i, j, 2**i-1, 2**j-1)

    defect = 2**j-1 - n
    parts = 2**(i-1)
    no_defect = int(2**j / parts) - 1
    # print(n, parts, no_defect)
    # print("parts, defect", parts, defect)

    import math
    ave_defect = math.floor(defect / parts)
    # print("totaldefect", defect)
    # print("nodefect", no_defect)
    # print("ave_defect", ave_defect)

    y = 0
    z = 0

    rank = k - 2**(i-1)
    # print("rank, max", rank, defect%parts)
    if rank < parts - defect%parts:
        t= no_defect - ave_defect
    else:
        t= no_defect - ave_defect -1
    # print(t)
    if t is 0:
        y, z = 0, 0
    elif t % 2 is 0:
        y, z = t/2, t/2-1
    else:
        y, z = (t-1)/2, (t-1)/2
    # print(spaces, y, z)

    # t1 = time.time()
    # print(t1-t0)
    print("Case #{}: {} {}".format(case, int(y), int(z)))

