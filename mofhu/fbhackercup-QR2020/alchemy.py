ncase = int(input())

for case in range(1, ncase + 1):
    n = int(input())
    s = input()
    a = 0

    for i in s:
        if i == 'A':
            a += 1
    b = n - a
    if abs(a-b) == 1:
        ans = 'Y'
    else:
        ans = 'N'
    print('Case #{}: {}'.format(case, ans))

