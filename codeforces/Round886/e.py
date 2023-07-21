# author: mofhu@github
# E. Cardboard for Pictures

t = int(input())

for ncase in range(1, t+1):
    n, c = [int(i) for i in input().split(' ')]
    s = [int(i) for i in input().split(' ')]
    s1 = sum(s)
    s2 = sum([i*i for i in s])

    from math import sqrt
    w = (-2*s1 + sqrt(4*s1*s1 - 4*n*(s2-c)))/4 / n

    print(int(w))




