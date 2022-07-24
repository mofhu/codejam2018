ncase = int(input())

for i in range(1, ncase+1):
    line = input()
    b, dot = 0,0
    n = len(line) - 1
    for s in line:
        if s == 'B':
            b += 1
        elif s == '.':
            dot += 1
    # print(n,b,dot)
    if b == 1 and n == 2:
        ans = 'Y'
    elif b > 1 and b != n:
        ans = 'Y'
    else:
        ans = 'N'

    print('Case #{}: {}'.format(i, ans))
