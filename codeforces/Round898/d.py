# author: mofhu@github
# D. 1D Eraser

t = int(input())

for ncase in range(1, t+1):
    n, k = [int(s) for s in input().split(' ')]
    a = input()
    ans = 0
    i = 0
    while i < n:
        if a[i] == 'B':
            ans += 1
            i += k
        else:
            i += 1


    print(ans)

