# author: mofhu@github
# Building Race

t = int(input())
for ncase in range(t):
    a, b, x, y = [int(s) for s in input().split(' ')]
    ta = (a) / x
    tb = (b) / y
    if ta == tb:
        ans = 'Both'
    elif ta < tb:
        ans = 'Chef'
    else:
        ans = 'Chefina'
    print(ans)
