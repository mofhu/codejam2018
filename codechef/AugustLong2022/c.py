# author: mofhu@github
# Make A and B equal

t = int(input())
for ncase in range(t):
    a, b = [int(s) for s in input().split(' ')]
    if a > b:
        a, b = b, a
    while a < b:
        a *= 2
    if a == b:
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)

