# author: mofhu@github
# A. Lucky?

ncase = int(input())

for case in range(1, ncase+1):
    s = [int(s) for s in input()]

    if sum(s[:3]) == sum(s[3:]):
        ans = 'YES'
    else:
        ans = 'NO'
    print(f'{ans}')
