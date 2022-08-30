# author: mofhu@github

t = int(input())

for ncase in range(1, t+1):
    # count all letters
    n = int(input())
    s = input()

    ans = 0
    flag = 0
    for i in range(n):
        if s[i] == 'O' or s[i] == 'X':
            if flag == 0:
                flag = s[i]
            if flag and flag != s[i]:
                ans += 1
                flag = s[i]

    # output
    print('Case #{}: {}'.format(ncase, ans))
