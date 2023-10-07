# author: mofhu@github
# B. Aleksa and Stack

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    i = 5
    ans = [str(i) for i in range(5,5+n)]

    print(' '.join(ans))


