# author: mofhu@github
# Colliding Encoding

ncase = int(input())

for case in range(1, ncase+1):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = [i for i in input().split(' ')]
    d = {a[i]: s[i] for i in range(len(a))}
    n = int(input())
    dw = set()
    ans = 'NO'
    for i in range(n):
        w = input()
        ww = ''.join([d[j] for j in w])
        if ww in dw:
            ans = 'YES'
            # print(dw, ww)
            # break
        else:
            dw.add(ww)
    print(f'Case #{case}: {ans}')
    # print(d)
    # print(dw)
