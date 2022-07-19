# author: mofhu@github
# Bidding

t = int(input())
for ncase in range(t):
    a, b, c = [int(s) for s in input().split(' ')]
    if max(a, b, c) == a:
        print('Alice')
    elif max(a, b, c) == b:
        print('Bob')
    else:
        print('Charlie')
