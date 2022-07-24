# author: mofhu@github
# C. Cypher

n0 = int(input())

for ncase in range(1, n0+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    for i in range(n):
        bi, b = input().split(' ')
        t = 0
        for j in b:
            if j == 'D':
                t += 1
            else:
                t -= 1
        a[i] = (a[i] + t) % 10


    print(' '.join([str(i) for i in a]))
