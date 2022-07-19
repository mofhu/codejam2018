# author: mofhu@github

t = int(input())

for ncase in range(1, t+1):
    # count all letters
    n = int(input())
    rows = []
    xrow = [0 for i in range(n)]
    xcol = [0 for i in range(n)]
    orow = [0 for i in range(n)]
    ocol = [0 for i in range(n)]
    drow = [0 for i in range(n)]
    dcol = [0 for i in range(n)]
    for i in range(n):
        row = input()
        rx = 0
        ro = 0
        rd = 0
        rows.append(row)
        for j in range(n):
            if row[j] == 'X':
                rx += 1
                xcol[j] += 1
            elif row[j] == 'O':
                ro = 1
                ocol[j] += 1
            else:
                rd += 1
                dcol[j] += 1
        xrow[i] = rx
        orow[i] = ro
        drow[i] = rd
    ans = [0 for i in range(2*n)]
    for i in range(n):
        if orow[i] == 0:
            ans[i] = n - xrow[i]
    for i in range(n):
        if ocol[i] == 0:
            ans[n+i] = n - xcol[i]
    # print(ans)
    if sum(ans) == 0:
        ans = 'Impossible'
    else:
        # print(ans)
        m = max(ans)
        for i in range(2*n):
            if ans[i] != 0:
                if ans[i] < m:
                    m = ans[i]
        ans0 = m
        ans1 = 0
        for i in ans:
            if i == ans0:
                ans1 += 1
        if ans0 == 1:
            # print(ans)
            # print(rows)
            for i in range(n):
                if ans[i] == 1 and ans[i+n] == 1 and rows[i][i] == '.':
                    ans1 -= 1
        ans = '{} {}'.format(str(ans0), str(ans1))




    # output
    print('Case #{}: {}'.format(ncase, ans))
