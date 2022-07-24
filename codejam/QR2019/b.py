# author: mofhu@github
# You Can Go Your Own Way

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    p = input()
    ans = ""
    x, y = 0, 0
    x1, y1 = 0, 0
    for i in range(len(p)):
        # print(x,y,p[i], x1, y1)
        if x == x1 and y == y1:
            flag = True
        if p[i] is "E":
            x += 1
            if flag:
                y1 += 1
                ans += "S"
                continue
        else:
            y += 1
            if flag:
                x1 += 1
                ans += "E"
                continue
        if x1 == n-1:
            y1 += 1
            ans += "S"
        elif y1 == n-1:
            x1 += 1
            ans += "E"
        else:
            if x1 == n-2:
                y1 += 1
                ans += "S"
            elif y1 == n-2:
                x1 += 1
                ans += "E"
            else:
                y1 += 1
                ans += "S"


    # print(mat)

    print("Case #{}: {}".format(case, ans))


