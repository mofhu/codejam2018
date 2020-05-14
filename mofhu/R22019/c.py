# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    m = []
    for i in range(n):
        x, y = (int(s) for s in input().split(" "))
        m.append((x,y))
    # print(m)
    flag = False
    left = 0
    right = 99999999999

    for k in range(n-1):
        # print(k, left, right)  # check bound
        i0 = m[k][0]
        j0 = m[k+1][0]
        i1 = m[k][1]
        j1 = m[k+1][1]
        # print(i0, j0, i1, j1)
        # i[0] mc + i[1] mj < j[0] mc + j[1] mj
        if i0 < j0 and i1 <= j1:
            pass
        elif i0 <= j0 and i1 < j1:
            pass
        elif i0 >= j0 and i1 >= j1:
            ans = 'IMPOSSIBLE'
            flag = True
        elif i0 < j0 and i1 > j1:
            # i1-j1 mj < j0-i0 mc
            left1 = (i1-j1)/(j0-i0)
            if left1 > left:
                left = left1
        else:
            # i0-j0 mc < j1-i1 mj
            right1 = (j1-i1)/(i0-j0)
            if right1 < right:
                right = right1
        if left >= right:
            ans = 'IMPOSSIBLE'
            flag = True
        # if i0 < j0 and i1 < j1 pass
        # if i0 >= j0 and i1 >= j1 impossible
        # if i0 < j0 and i1 > j1,
        # if i0 > j0 and i1 < j1
        if flag is True:
            ans = 'IMPOSSIBLE'
            break
    else:
        # print(left, right)  # check bound
        i = 1
        j = 1
        while flag is False:
            if i/j > left and i/j < right:
                flag = True
            elif i/j >= right:
                j += 1
            elif i/j <= left:
                i += 1
                j = 1
        ans = '{} {}'.format(i,j)

    # print(left, right)  # check bound

    print("Case #{}: {}".format(case, ans))


