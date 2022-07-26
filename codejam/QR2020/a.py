ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    trace = 0
    row = 0
    col = 0
    m_row = []
    for i in range(n):
        t = [int(s) for s in input().split(' ')]
        # print(t)
        for j in range(n):
            flag = 0
            for k in range(j+1, n):
                if t[j] == t[k]:
                    row += 1
                    flag = 1
                    break
            if flag == 1:
                break
        m_row.append(t)
    # print(m_row)  #
    for i in range(n):
        trace += m_row[i][i]
        t = [m_row[s][i] for s in range(n)]
        # print(t)
        for j in range(n):
            flag = 0
            for k in range(j+1, n):
                if t[j] == t[k]:
                    col += 1
                    flag = 1
                    break
            if flag == 1:
                break


    print("Case #{}: {} {} {}".format(case, trace, row, col))

    # print(d2)

