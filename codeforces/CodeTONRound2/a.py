# author: mofhu@github
# A. Two 0-1 sequences

t = int(input())

for ncase in range(1, t+1):
    n, m = [int(s) for s in input().split(' ')]
    a = input()
    b = input()
    if m == 1:
        if a[-1] == b[-1]:
            ans = 'YES'
        else:
            if '0' in a and '1' in a:
                ans = 'YES'
            else:
                ans = 'NO'
    else:
        if a[1-m:] != b[1:]:
            ans = 'NO'
        elif a[-m] == b[0]:
            ans = 'YES'
        else:
            if '0' in a[:1-m] and '1' in a[:1-m]:
                ans = 'YES'
            else:
                ans = 'NO'
    print(ans)
