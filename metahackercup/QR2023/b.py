# author: mofhu@github
# B: Dim Sum Delivery

ncase = int(input())

for t in range(1, ncase + 1):
    r, c, a, b = [int(s) for s in input().split(' ')]
    if r > c:
        ans = 'YES'
    else:
        ans = 'NO'
    print('Case #{}: {}'.format(t, ans))

