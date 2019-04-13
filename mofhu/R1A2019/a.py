ncase = int(input())

for case in range(1, ncase+1):
    r, c = [int(s) for s in input().split(" ")]

    blank = [0 for s in range(r*c)]

    r0, c0 = int(round((r-0.2)/2, 0)), int(round((c-0.2)/2, 0))
    #rint("r0c0", r0, c0)  #

    blank[r0*c+c0] = 1
    # print(blank)
    from collections import deque
    from math import floor
    status = deque()
    move = 1
    moves = [(r0, c0)]
    status.append((r0, c0, move, blank.copy(), moves.copy()))

    ans = "IMPOSSIBLE"
    while(len(status) > 0):
        if move == r*c:
            ans = "POSSIBLE"
            ansmove = moves
            break
        r1, c1, move, occ, moves = status.pop()
        # print(r1, c1, move, occ)  #
        for i in range(len(occ)):
            if occ[i] == 0:
                ci = i % c
                ri = 0
                rt = i
                while rt - c >= 0:
                    rt = rt-c
                    ri += 1
                if ri != r1 and ci != c1:
                    if ri-ci != r1-c1 and ri+ci != r1+c1:
                        # print("add", ri, ci) #
                        occ1 = occ.copy()
                        occ1[i] = 1
                        moves1 = moves.copy()
                        moves1.append((ri,ci))
                        status.append((ri, ci, move+1, occ1, moves1))

    print("Case #{}: {}".format(case, ans))
    if ans ==  "POSSIBLE":
        for i in moves:
            print(str(i[0]+ 1) + " " + str(i[1]+ 1))

    # print(d2)

