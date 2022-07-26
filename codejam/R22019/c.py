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
    left = (0,1)
    right = (99999999999,1)

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
            if left1 > left[0]/left[1]:
                left = ((i1-j1), (j0-i0))
        else:
            # i0-j0 mc < j1-i1 mj
            right1 = (j1-i1)/(i0-j0)
            if right1 < right[0]/right[1]:
                right = ((j1-i1), (i0-j0))
        if left[1]*right[0] <= left[0]*right[1]:
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
        #  print(left, right)  # check bound
        if right[0] == 1 and right[1] == 1:
            ans = 'IMPOSSIBLE'
        elif left[0] is 0:
            ans = '1 1'
        else:
            from math import floor
            """
            c = int(left[0] * right[0] / gcd(left[0], right[0]))
            rl = int(c / left[0])
            rr = int(c / right[0])
            delta = rl*left[1] - rr*right[1]
            """
            # print(delta)
            c = 1
            j = int(floor(left[1] * c / left[0]))
            if j == 0:
                j = 1
            if c *left[1] == j*left[0]:
                c += 1
            while (True):
                # print(c, j)
                if c/j < right[0]/right[1]:
                    break
                else:
                    c += 1
                    j = int(floor(left[1] * c / left[0]))
            ans = '{} {}'.format(c, j)

    # print(left, right)  # check bound

    print("Case #{}: {}".format(case, ans))


