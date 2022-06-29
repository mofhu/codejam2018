# author: mofhu@github
# Make all equal using Pairs

t = int(input())
for ncase in range(t):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    count = {}
    maxc = 0
    for i in a:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > maxc:
            maxc = count[i]
    print(n-maxc)
