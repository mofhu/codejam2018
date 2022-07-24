# author: mofhu@github
# only for test set 1 and 2

ncase = int(input())

for case in range(1, ncase+1):
    x, y, s = input().split(' ')
    x, y = int(x), int(y)
    s = list(s)
    ans = 0
    s0 = '?'
    for i in range(len(s)):
        if s[i] != '?':
            s0 = s[i]
        else:
            s[i] = s0
    for i in range(1, len(s)):
        if s[i-1] == 'C' and s[i] == 'J':
            ans += x
        elif s[i-1] == 'J' and s[i] == 'C':
            ans += y

    print("Case #{}: {}".format(case, ans))


