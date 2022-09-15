# author: mofhu@github
# A. Two Elevators

t = int(input())

for ncase in range(1, t+1):
    a, b, c = [int(s) for s in input().split(' ')]
    t0 = abs(a-1)
    t1 = abs(c-b) + abs(c-1)
    if t0 < t1:
        ans = '1'
    elif t0 > t1:
        ans = '2'
    else:
        ans = '3'
    print(ans)

