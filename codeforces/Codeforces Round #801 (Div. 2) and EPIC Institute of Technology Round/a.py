# author: mofhu@github
# A - Subrectangle Guess

ncase = int(input())

for case in range(1, ncase+1):
    n, m = [int(i) for i in input().split(' ')]
    a = []
    for i in range(n):
        ai = [int(s) for s in input().split(' ')]
        a.append(ai)
    a0 = a[0][0]
    mi, mj = 0, 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > a0:
                a0 = a[i][j]
                mi, mj = i, j
    # print(mi, mj)
    rowi = max(mi+1, n-mi)
    rowj = max(mj+1, m-mj)
    # print(rowi, rowj)
    print(rowi*rowj)
