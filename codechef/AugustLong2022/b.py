# author: mofhu@github
# Sale Season

t = int(input())
for ncase in range(t):
    x = int(input())
    if x <= 100:
        ans = x
    elif x <= 1000:
        ans = x - 25
    elif x <= 5000:
        ans = x - 100
    else:
        ans = x - 500
    print(ans)
