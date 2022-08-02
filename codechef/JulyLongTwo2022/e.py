# author: mofhu@github
# Sum of Product 1

t = int(input())
for ncase in range(t):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    a.append(0)
    ans = 0
    l = 0
    flag = True
    for i in range(n+1):
        if a[i] == 0:
            ans += l * (l+1) // 2
            flag = False
            l = 0
        else:  # a[i] == 1
            if flag == False:
                flag = True
                l = 1
            else:
                l += 1

    print(ans)


