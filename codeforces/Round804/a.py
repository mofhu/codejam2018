# author: mofhu@github
# A. The Third Three Number Problem

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    if n % 2 == 1:
        ans = -1
    else:
        ans = f'{n//2} 0 0'
    print(ans)

