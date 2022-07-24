ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(s) for s in input().split(" ")]
    value = [int(s) for s in input().split(" ")]
    value.sort()
    # print(value)

    ev0 = sum(value) / len(value)
    # print(ev0)

    ev = 0
    if k == 0 or n == 1:
        ev = ev0
    else:
        i = 0
        while(i < n):
            value1 = value[:]
            del value1[i]
            ev1 = sum(value1) / (len(value) - 1)
            if value[i] > ev1:
                # keep it
                ev += value[i] / n
            else:
                ev += ev0 / n
            i += 1
    print("Case #{}: {}".format(case, ev))

