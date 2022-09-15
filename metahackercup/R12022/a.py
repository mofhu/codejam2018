# author: mofhu@github
# A1: Consecutive Cuts - Chapter 1

ncase = int(input())

for t in range(1, ncase + 1):
    n, k = [int(s) for s in input().split(' ')]
    a = [int(s) for s in input().split(' ')]
    b = [int(s) for s in input().split(' ')]
    # k=0 / k!=0
    if k == 0:
        for i in range(n):
            if a[i] != b[i]:
                ans = 'NO'
                break
        else:
            ans = 'YES'
    else:
        shift = 0
        for i in range(n):
            if a[0] == b[i]:
                shift = i
        if k == 1 and shift == 0:
            ans = 'NO'
        elif n == 2 and shift % 2 != k % 2:
                ans = 'NO'
        else:
            for i in range(1, n):
                if shift + i < n:
                    if a[i] != b[shift + i]:
                        ans = 'NO'
                        break
                else:
                    if a[i] != b[shift + i - n]:
                        ans = 'NO'
                        break
            else:
                ans = 'YES'
    # print(n, k, a, b)

    print('Case #{}: {}'.format(t, ans))
