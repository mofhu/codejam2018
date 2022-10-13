# author: mofhu@github
# B. Funny Permutation

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    if n == 2:
        ans = '2 1'
    elif n == 3:
        ans = '-1'
    elif n % 2 == 0:
        ans = ' '.join([str(i) for i in range(n, 0, -1)])
    else:
        ans = ' '.join([str(i) for i in range(n, int((n+1)/2), -1)] + [str(i) for i in range(1, int((n+3)/2))])


    print(ans)


