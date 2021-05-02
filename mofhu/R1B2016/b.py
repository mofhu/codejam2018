ncase = int(input())

import re

for case in range(1, ncase+1):
    c, j = input().split(" ")

    cs = [c]
    # print(cs)
    def ques(cs):
        while "?" in cs[-1]:
            t = cs[-1]
            del cs[-1]
            # print(t)
            j = re.split('\?', t)
            # print(j)
            if len(j) == 2:
                for i in range(0,10):
                    newj = str(i).join(j)
                    cs.append(newj)
            elif len(j) == 3:
                for i in range(0, 10):
                    for k in range(0, 10):
                        newj = j[0] + str(i) + j[1] + str(k) + j[2]
                        cs.append(newj)
            elif len(j) == 4:
                cs = [str(i) + str(k) + str(l) for i in range(10) for k in range(10) for l in range(10)]
        return cs
        # print(cs)
    cs = ques(cs)
    # print(cs)
    js = [j]
    js = ques(js)
    # print(js)
    best_diff = 9999
    best_c = 9999
    best_j = 9999
    c0 = 0
    j0 = 0
    def caldiff(c,j):
        return (abs(int(c)-int(j)), int(c), int(j))

    # print(caldiff(19, 20))
    # print(caldiff(19, 30))

    for c in cs:
        for j in js:
            result = caldiff(c,j)
            if (result[0] < best_diff or
                (result[0] == best_diff and result[1] < best_c) or
                (result[0] == best_diff and result[1] == best_c and result[2] < best_j)):
                best_diff, best_c, best_j = result[0], result[1], result[2]
                # print(best_diff, result)
                c0 = c
                j0 = j

    print("Case #{}: {} {}".format(case, c0, j0))

