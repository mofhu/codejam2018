# author: mofhu@github
# A - Double Click

n, d = [int(i) for i in input().split(' ')]
t = [int(i) for i in input().split(' ')]

ans = -1
for i in range(1, n):
    if t[i] - t[i-1] <= d:
        ans = t[i]
        print(ans)
        break
else:
    print(ans)
