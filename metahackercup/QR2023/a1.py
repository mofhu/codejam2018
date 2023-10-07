# author: mofhu@github
# A1: Cheeseburger Corollary 1

ncase = int(input())

for t in range(1, ncase + 1):
    s, d, k = [int(s) for s in input().split(' ')]
    if 2*s + 2*d >= k+1 and s + 2*d >= k:
        ans = 'YES'
    else:
        ans = 'NO'
    print('Case #{}: {}'.format(t, ans))
