# author: mofhu@github
# Chef Drinks Tea

t = int(input())
for i in range(t):
    x, y, z = [int(s) for s in input().split(' ')]
    n_count = 0
    while y * n_count < x:
        n_count += 1
    print(f'{z * n_count}')
