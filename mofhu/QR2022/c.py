# author: mofhu@github
# d1000000

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    s = sorted(s)
    # print(s)
    ans = 0
    for i in range(n):
        if s[i] > ans:
            ans += 1
    print("Case #{}: {}".format(case, ans))
