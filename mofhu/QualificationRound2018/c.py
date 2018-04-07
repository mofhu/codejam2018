ncase = int(input())

# f = open("test.out", "w")
from collections import deque


for case in range(1, ncase+1):
    a = int(input())
    # f.write(str(a) + "\n")
    if a == 200:
        target_ij = []
        for x in range(501, 509):
            for y in range(501, 519):
                target_ij.append((x, y))
    elif a == 20:
        target_ij = [
            (501, 501), (501, 503),
            (502, 501), (502, 503),
        ]
    go = deque()
    for pos in target_ij:
        ij_sum = 0
        go.append(pos)
    s = [0] * 200

    min_status = 0
    while(len(pos) != 0):
        pos = go.popleft()
        i,j = pos[0] - 500, pos[1] - 500
        if a == 200:
            x = 20
        if a == 20:
            x = 5
        def gen_ij(i,j):
            d = [
                (i-1,j-1), (i-1, j), (i-1, j+1),
                (i,j-1), (i, j), (i, j+1),
                (i+1,j-1), (i+1, j), (i+1, j+1),
            ]
            # print("# ",d)
            d1 = [(x*i)+j for i,j in d]
            # print("# ",d1)
            return d1
        d1 = gen_ij(i,j)
        status = sum(s[near] for near in d1)
        # print("# ", i, j, status, min_status)

        if status == 9:
            # del pos with pop
            continue
        elif status > min_status:
            # pass
            go.append(pos)
            continue
        else:
            print(pos[0], pos[1])
            i1, j1 = [int(s) for s in input().split(" ")]
            if i1 == 0 and j1 == 0:
                break

            s[(i1-500)*x + j1-500] = 1
            d2 = gen_ij(i1-500,j1-500)
            min_status = sum(s[near] for near in d1)
            go.append(pos)
            # print(s)

