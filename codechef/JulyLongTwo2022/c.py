# author: mofhu@github
# Chef and Candies

t = int(input())
for ncase in range(t):
    x, y, n, r = [int(s) for s in input().split(' ')]
    if r < n*x:
        ans = -1
    elif r >= n*y:
        ans = f'0 {n}'
    else:  # both needed
        diff = r - n*x
        ny = diff // (y-x)
        nx = n - ny
        ans = f'{nx} {ny}'
    print(ans)

