# author: mofhu@github
# B1: Second Friend

ncase = int(input())

for t in range(1, ncase + 1):
    r, c = [int(s) for s in input().split(' ')]
    d = []
    tree = {}
    for i in range(r):
        d.append(input())
    # print(d)
    ans = 'Possible'
    if r == 1 or c == 1:
        for row in d:
            if '^' in row:
                ans = 'Impossible'
                break
    else:  # must have answer
        d = ['^' * c] * r

    print('Case #{}: {}'.format(t, ans))
    if ans == 'Possible':
        for i in range(r):
            print(''.join(d[i]))

