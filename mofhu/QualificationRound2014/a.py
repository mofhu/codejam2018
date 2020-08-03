ncase = int(input())
import re

# print(ncase)

for case in range(1, ncase+1):

    row1 = int(input())
    nums1 = []
    for i in range(4):
        if i == row1 - 1:
            nums1 = [int(j) for j in re.findall("\d+", input())]
        else:
            t = input()
    # print(nums1)

    row2 = int(input())
    nums2 = []
    for i in range(4):
        if i == row2 - 1:
            nums2 = [int(j) for j in re.findall("\d+", input())]
        else:
            t = input()
    # print(nums2)
    join = []
    for num in nums1:
        if num in nums2:
            join.append(num)
    # print(join)
    if len(join) == 1:
        print("Case #{}: {}".format(case, join[0]))
    elif len(join) == 0:
        print("Case #{}: Volunteer cheated!".format(case))
    else:
        print("Case #{}: Bad magician!".format(case))

