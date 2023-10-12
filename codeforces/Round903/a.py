# author: mofhu@github
# A. Don't Try to Count

t = int(input())

for ncase in range(1, t+1):
    n, m = [int(s) for s in input().split(' ')]
    x = input()
    s = input()
    for i in range(110):
        if s in x:
            ans = i
            break
        else:
            x = x + x
            if len(x) > 110 * m:
                ans = -1
                break
    else:
        ans = -1
    print(ans)




