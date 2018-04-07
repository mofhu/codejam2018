ncase = int(input())

# f = open("test.out", "w")

for case in range(1, ncase+1):
    a = int(input())
    # f.write(str(a) + "\n")
    target_ij = [
        (500, 500),
        (500, 501),
        (502, 500),
        (502, 501),
    ]

    flag = False
    for pos in target_ij:
        i, j = pos
        ij_sum = 0
        dij = {
            (i-1,j-1): 0,
            (i-1,j): 0,
            (i-1,j+1): 0,
            (i,j-1): 0,
            (i,j): 0,
            (i,j+1): 0,
            (i+1,j-1): 0,
            (i+1,j): 0,
            (i+1,j+1): 0,
            }
        while(ij_sum < 9):
            print(i, j)
            i1, j1 = [int(s) for s in input().split(" ")]
            # f.write(str(i1) + str(j1) + "\n")
            # f.write(str(ij_sum) + "\n")
            if i1 == 0 and j1 == 0:
                flag = True
                break
            elif dij[(i1,j1)] == 0:
                dij[(i1, j1)] = 1
                ij_sum += 1
        if flag is True:
            break
    if flag is True:
        continue

