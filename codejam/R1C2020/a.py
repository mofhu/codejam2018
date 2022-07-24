ncase = int(input())

for case in range(1, ncase+1):
    x, y, m = [s for s in input().split(' ')]
    x = int(x)
    y = int(y)
    posp = [(x,y)]
    for i in range(len(m)):
        if m[i] is 'N':
            y += 1
            posp.append((x,y))
        elif m[i] is 'S':
            y -= 1
            posp.append((x,y))
        elif m[i] is 'E':
            x += 1
            posp.append((x,y))
        elif m[i] is 'W':
            x -= 1
            posp.append((x,y))
    ans = 'IMPOSSIBLE'
    for j in range(1, len(m)+1):
        # print(j, posp[j][0] + posp[j][1])
        # print(j, posp[j][0] , posp[j][1])
        if j >= abs(posp[j][0]) + abs(posp[j][1]):
            ans = j
            break



    print("Case #{}: {}".format(case, ans))


