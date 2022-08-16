# author: mofhu@github
# Two Trains

t = int(input())
for ncase in range(t):
    n = int(input())
    p = [int(s) for s in input().split(' ')]

    s = 0
    delay = 0

    for i in p:
        s += i
        if delay < i:
            delay = i
    print(s + delay)
