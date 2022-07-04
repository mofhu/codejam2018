# author: mofhu@github
# High Accuracy

t = int(input())
for ncase in range(t):
    x = int(input())
    ans = x % 3
    if ans != 0:
        ans = 3 - ans
    print(f'{ans}')
