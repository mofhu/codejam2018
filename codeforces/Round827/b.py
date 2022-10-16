# author: mofhu@github
# B. Increasing

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    abc = [int(s) for s in input().split(' ')]
    abc.sort()
    for i in range(len(abc)-1):
        if abc[i] == abc[i+1]:
            print('NO')
            break
    else:
        print('YES')


