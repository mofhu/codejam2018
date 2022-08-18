# author: mofhu@github
# B. Optimal Reduction

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    flag = 0
    change = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            if flag == '+':
                change += 1
            flag = '-'
        elif a[i] < a[i+1]:
            if flag == '-':
                change += 1
            flag = '+'
        if change > 1:
            ans = 'NO'
            break
        # print(i, flag, change)
    else:
        if change == 1 and flag == '+':
            ans = 'NO'
        else:
            ans = 'YES'
    print(ans)


