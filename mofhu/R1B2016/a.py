ncase = int(input())

d = {
    0: {'Z':1, 'E':1, 'R':1, 'O':1},
    1: {'O':1, 'N':1, 'E':1},
    2: {'T':1, 'W':1, 'O':1},
    3: {'T':1, 'H':1, 'R':1, 'E':2},
    4: {'F':1, 'O':1, 'U':1, 'R':1},
    5: {'F':1, 'I':1, 'V':1, 'E':1},
    6: {'S':1, 'I':1, 'X':1},
    7: {'S':1, 'E':2, 'V':1, 'N':1},
    8: {'E':1, 'I':1, 'G':1, 'H':1, 'T':1},
    9: {'N':1, 'I':1, 'N':1, 'E':1},
    }

for case in range(1, ncase+1):
    s = input()

    d2 = {}
    for digit in d:
        for letter in d[digit]:
            if letter not in d2:
                d2[letter] = 0
    for letter in s:
        d2[letter] += 1
    # print(d2)

    from pulp import *
    # IP
    digits = [i for i in range(0, 10)]
    # print(digits)
    prob = LpProblem("case", LpMaximize)
    prob += 0, "no need for max"
    x = LpVariable.dicts("Choice",(digits),0,1000,LpInteger)
    # print(x)

    # for i in prob.variables():
    #     print(i.name)
    # equations:
    m = {}
    for l in d2:
        m[l] = {}
        for digit in d:
            if l in d[digit]:
                m[l][digit] = d[digit][l]
            else:
                m[l][digit] = 0
    # print(m)

    for l in d2:
        prob += lpSum([x[digit] * m[l][digit] for digit in digits]) == d2[l], "{}".format(l)

    prob.writeLP("a.lp")  # output LP
    prob.solve(COIN_CMD())

    ans = []
    j = 0
    for i in prob.variables():
        # print(i.name, i.varValue)
        if i.varValue:
            if int(i.varValue) > 0:
                ans.append(int(i.varValue) * str(j))
        j += 1
    print("Case #{}: ".format(case) + "".join(ans))
"""
    for r, c in rc:
        prob += lpSum([choices[v][r][c] for v in vals]) <= 1, ""#"one in cell {},{}".format(r,c)
    prob.solve(GUROBI_CMD(msg=False))
"""
