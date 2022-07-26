# author: mofhu@github
# A. XOR Mixup

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    ans = 0
    for i in range(len(a)):
        xor = [a[j] for j in range(len(a)) if j != i]
        if len(xor) > 1:
            x = xor[0]
            for j in xor[1:]:
                x = x^j
        else:
            x = xor[0]
        if a[i] == x:
            ans = a[i]
            print(f'{ans}')
            break




