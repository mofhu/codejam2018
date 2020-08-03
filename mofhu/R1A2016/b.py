ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    d = {}
    for i in range(2*n - 1):
        s = [int(s) for s in input().split(" ")]
        for num in s:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
    # print(d)  # debug
    s = []
    for num in d:
        if d[num] % 2 == 1:
            s.append(num)
    s = sorted(s)
    s = [str(num) for num in s]

    print("Case #{}: {}".format(case, " ".join(s)))



