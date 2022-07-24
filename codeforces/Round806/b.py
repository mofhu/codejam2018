# author: mofhu@github
# B. Permutation

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s = input()
    d = set()
    ans = 0
    for i in s:
        if i not in d:
            ans += 2
            d.add(i)
        else:
            ans += 1
    print(f'{ans}')


