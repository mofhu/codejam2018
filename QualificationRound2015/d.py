t = int(input())

rwin2 = set([11, 13, 33])
rwin3 = set([11, 12, 13, 14, 22, 24, 44])
rwin4 = set([11, 12, 13, 14,
            22, 23, 24, 33])

for ncase in range(1, t+1):
    x, r, c = [int(s) for s in input().split(" ")]
    if r > c:
        r, c = c, r
    if x is 1:
        winner = "GABRIEL"
    elif x is 2:
        if r*10+c in rwin2:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    elif x is 3:
        if r*10+c in rwin3:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    elif x is 4:
        if r*10+c in rwin4:
            winner = "RICHARD"
        else:
            winner = "GABRIEL"
    print("Case #{}: {}".format(ncase, winner))
