# author: mofhu@github
# A. NIT orz!

ncase = int(input())

for case in range(1, ncase+1):
    n, z = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    ans = 0
    for ai in a:
        t = ai | z
        if t > ans:
            ans = t
    print(f'{ans}')
