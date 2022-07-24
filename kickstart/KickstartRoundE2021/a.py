# author: mofhu@github
# only for test set 1 and 2
# note after AC: should be able to notice that this is a sorting problem.
# see google's analysis for details.

ncase = int(input())

for case in range(1, ncase+1):
    s = input()
    d = {}
    pos = {}
    i = 0
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
            pos[s[i]] = [i]
        else:
            d[s[i]] += 1
            pos[s[i]].append(i)
    sortd = []
    for i in d:
        sortd.append((d[i], i))

    sortd = sorted(sortd, reverse=True)
    # print(sortd)
    # print(pos)
    ans = sortd[0]
    if sortd[0][0] * 2 > len(s):
        ans = 'IMPOSSIBLE'
    else:
        ans = ['z' for i in range(len(s))]
        occupied = [0 for i in range(len(s))]
        j = 0
        for i in range(len(sortd)-1, -1, -1):
            n, letter = sortd[i]
            # print(n, letter)
            # print(ans)
            for k in range(len(sortd)):
                if i != k:
                    for p in pos[sortd[k][1]]:
                        if n == 0:
                            break
                        if occupied[p] == 0:
                            occupied[p] = 1
                            n -= 1
                            ans[p] = letter
                if n == 0:
                    break
        ans = ''.join(ans)

    print("Case #{}: {}".format(case, ans))

