# author: mofhu@github
# B. Almost Ternary Matrix

ncase = int(input())

for case in range(1, ncase+1):
    n, m = [int(s) for s in input().split(' ')]
    flag = 0
    for i in range(n):
        if i % 4 == 0 or i % 4 == 3:
            if m % 4 == 0:
                print(' '.join(['1','0','0','1']* (m//4)))
            else:
                print('1 0'+' 0 1 1 0'*(m//4))
        else:
            if m % 4 == 0:
                print(' '.join(['0','1','1','0']* (m//4)))
            else:
                print('0 1' + ' 1 0 0 1' * (m//4))
