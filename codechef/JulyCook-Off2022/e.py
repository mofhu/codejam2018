# author: mofhu@github
# Xor Permutation

t = int(input())

for ncase in range(t):
    n = int(input())
    '''
    for i in range(200):
        # print(f'{i} {i+1} {i ^ i+1}')
        if i ^ i+1 == i+2:
            print(f'{i} {i+1} {i ^ i+1}')
            print('!')
    break
    '''
    if n == 3:
        ans = -1
    else:
        ans = '1 4 3 2'
        for i in range(5, n+1):
            ans += ' ' + str(i)
    print(ans)


