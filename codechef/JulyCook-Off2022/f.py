# author: mofhu@github
# Permutation And Median

t = int(input())

for ncase in range(t):
    n = int(input())
    s = []
    for i in range(n):
        if i % 2 == 1:
            s.append(str(i//2+1))
        else:
            s.append(str(n-i//2))
    print(' '.join(s))
    # cal test
    '''
    s1 = [int(i) for i in s]
    for i in range(n):
        s10 = sorted(s1[:i+1])
        print('s10', s10)
        if i % 2 == 1:
            print('i=', i, s10[i//2])
        else:
            print('i=', i,s10[i//2])
    '''


