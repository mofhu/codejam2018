# author: mofhu@github
# A. Sum

t = int(input())

for ncase in range(1, t+1):
    abc = [int(s) for s in input().split(' ')]
    abc.sort()
    # print(abc)
    if abc[0] + abc[1] == abc[2]:
        print('YES')
    else:
        print('NO')




