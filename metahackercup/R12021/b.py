# author: mofhu@github

t = int(input())

for ncase in range(1, t+1):
    # count all letters
    n, m, a, b = [int(s) for s in input().split(' ')]
    if n+m-1 > a or n+m-1 > b:
        ans = 'Impossible'
    else:
        ans = 'Possible'
    # output
    print('Case #{}: {}'.format(ncase, ans))
    if ans == 'Possible':
        firstrow = [a-n-m+2] + [1] * (m-2) + [b-n-m+2]
        print(' '.join([str(i) for i in firstrow]))
        row = ['1'] * m
        for i in range(1, n):
            print(' '.join(row))

