ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    # print(n,k)
    # print(a)
    # generate max consume
    a.sort()
    # print(a)
    m = []
    for i in range(1, n+1):
        if len(m) <= n:
            m += [i] * k
        else:
            break
    # print(m)
    ans = 0
    i = 0
    j = 0
    flag = False
    while i < len(a) and j < len(m):
        # print(i,j)
        while a[i] < m[j]:
            if i < len(a)-1:
                i += 1
            else:
                flag = True
                break
        if flag is True:
            break
        # print(i,j)
        if a[i] >= m[j]:
            ans += 1
            i += 1
            j += 1
    print("Case #{}: {}".format(case, ans))

