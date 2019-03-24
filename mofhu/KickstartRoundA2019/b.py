ncase = int(input())

for case in range(1, ncase+1):
    r, c = [int(s) for s in input().split(' ')]
    mat = []
    for i in range(r):
        mat.append([int(s) for s in input()])
    # print(mat)

    from copy import deepcopy
    def cal_min(mat):
        mat0 = deepcopy(mat)
        mat1 = deepcopy(mat)
        for t in range(r+c):
            flag = True
            flag11 = True
            # print(mat0)
            for i in range(r):
                for j in range(c):
                    # print(i, j)
                    if mat0[i][j] != 0:
                        # print(i,j, 1)  #
                        continue
                    else:
                        flag11 = False
                        if i > 0 and mat0[i-1][j] == 1:
                            # print(i,j, 'i-1')  #
                            mat1[i][j] = 1
                        elif j > 0 and mat0[i][j-1] == 1:
                            # print(i,j, 'j-1')  #
                            mat1[i][j] = 1
                        elif i < r-1 and mat0[i+1][j] == 1:
                            # print(i,j, 'i+1')  #
                            mat1[i][j] = 1
                        elif j < c-1 and mat0[i][j+1] == 1:
                            # print(i,j, 'j+1')  #
                            mat1[i][j] = 1
                        else:
                            # print("not ok")
                            flag = False  # not finishing
            if flag is True:
                if flag11 is True:
                    ans = t
                else:
                    ans = t + 1
                break
            else:
                mat0 = deepcopy(mat1)
        return ans

    ans0 = cal_min(mat)
    if ans0 is 0:
        print("Case #{}: {}".format(case, ans0))
        continue
    for i in range(r):
        for j in range(c):
            if mat[i][j] is 0:
                matij = deepcopy(mat)
                matij[i][j] = 1
                ans = cal_min(matij)
                if ans < ans0:
                    ans0 = ans
                    # print(matij)


    print("Case #{}: {}".format(case, ans0))

    # print(d2)

