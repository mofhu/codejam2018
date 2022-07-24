# author: mofhu@github
# Chef and Candies

t = int(input())
for ncase in range(t):
    n, x = [int(s) for s in input().split(' ')]
    if x >= n:
        ans = 0
    else:
        ans = 0
        while n-x > 4*ans:
            ans += 1
    print(ans)

