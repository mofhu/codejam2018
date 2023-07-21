# author: mofhu@github
# A. To My Critics

t = int(input())

for ncase in range(1, t+1):
    a, b, c = [int(i) for i in input().split(' ')]
    d = a+b
    f = b+c
    e = a+c
    if d < 10 and e < 10 and f < 10:
        ans = 'NO'
    else:
        ans = 'YES'
    print(ans)




