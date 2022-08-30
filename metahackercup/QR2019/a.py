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
    if 2*b >= n and b < n:
            ans = 'Y'
    else:
        ans = 'N'

    print('Case #{}: {}'.format(i, ans))
