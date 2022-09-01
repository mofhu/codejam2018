# author: mofhu@github
# D. Line

t = int(input())

# import re
for ncase in range(1, t+1):
    n = int(input())
    s = input()
    diff = []
    score = []
    s0 = 0
    for i in range(n):
        if s[i] == 'L':
            diff.append(n-i-1 - i)
            s0 += i
        else:
            diff.append(i - (n-i-1))
            s0 += n-1-i
        if diff[i] < 0:
            diff[i] = 0
        else:
            diff[i] = diff[i]
    diff.sort(reverse=True)
    # print(diff)
    score.append(s0)
    for i in range(1,n+1):
        score.append(score[i-1] + diff[i-1])
    print(' '.join((str(s)) for s in score[1:]))





