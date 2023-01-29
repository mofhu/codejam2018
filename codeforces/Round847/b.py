# author: mofhu@github
# B. Taisia and Dice

t = int(input())

for ncase in range(1, t+1):
    n, s, r = [int(s) for s in input().split(' ')]
    d = s - r
    ans = [d]
    while n - len(ans) > 1:
        if r - d >= n - len(ans) - 1:
            ans.append(d)
            r -= d
        else:
            ans.append(1)
            r -= 1
    else:
        ans.append(r)

    print(' '.join([(str(i)) for i in ans]))


