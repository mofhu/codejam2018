ncase = int(input())

for case in range(1, ncase+1):
    n, k = (int(s) for s in input().split(" "))
    a = [int(s) for s in input().split(" ")]

    t = k
    ans = 0
    for i in range(n):
        if a[i] != t:
            t = k
            if a[i] == k:
                t = k-1
        else:
            if t > 1:
                t -= 1
            else:
                ans += 1
                t = k

    print("Case #{}: {}".format(case, ans))


