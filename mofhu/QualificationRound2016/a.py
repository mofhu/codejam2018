t = int(input())

for case in range(1, t+1):
    n = int(input())
    if n is 0:
        print("Case #{}: INSOMNIA".format(case))
        continue
    nums = set([])
    n0 = n
    while True:
        digits = str(n)
        for d in digits:
            nums.add(d)
        if len(nums) < 10:
            n += n0
        else:
            break
    print("Case #{}: {}".format(case, n))

