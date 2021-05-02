n = int(input())

for case in range(1, n + 1):
    level, nums = [s for s in input().split(" ")]
    level = int(nums)
    # print(nums)

    y = 0
    i = 0
    stand = 0
    for people_i in nums:
        people_i = int(people_i)
        # print(i, people_i)
        if y + stand >= i:
            pass
        else:
            y = i - stand
        stand += people_i
        i += 1
    print("Case #{}: {}".format(case, y))

