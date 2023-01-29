# author: mofhu@github
# D. Matryoshkas

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    ans = {}
    a.sort()
    # print(a)
    for i in a:
        if i-1 in ans:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
            if ans[i-1] == 1:
                del ans[i-1]
            else:
                ans[i-1] -= 1
        else:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
    # print(ans)
    count = 0
    for i in ans:
        count += ans[i]
    print(count)




