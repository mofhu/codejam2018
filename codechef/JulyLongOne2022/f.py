# author: mofhu@github
# Game of Piles Version 1

t = int(input())
for ncase in range(t):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    if 1 in a:
        ans = 'CHEF'
    elif sum(a) % 2 != 0:
        ans = 'CHEF'
    else:
        ans = 'CHEFINA'
    print(ans)
