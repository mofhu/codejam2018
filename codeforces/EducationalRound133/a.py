# author: mofhu@github
# A. 2-3 Moves

ncase = int(input())

for case in range(1, ncase+1):
    n= int(input())
    y = n // 3
    if n % 3 != 0:
        x = 1
    else:
        x = 0
    if n == 1:
        y = 1

    print(f'{x+y}')
