# author: mofhu@github
# A. Grass Field

n = int(input())

for ncase in range(1, n+1):
    s = input()
    if s.upper() == 'YES':
        ans = 'YES'
    else:
        ans = 'NO'

    print(f'{ans}')
