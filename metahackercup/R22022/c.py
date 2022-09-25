# author: mofhu@github
# Problem C: Balance Scale

ncase = int(input())
mod = 1000000007

for t in range(1, ncase + 1):
    n, k = [int(s) for s in input().split(' ')]
    ans = 0
    c1, w1 = [int(s) for s in input().split(' ')]
    nlow = 0
    nsame = 0
    nhigh = 0
    for i in range(1, n):
        c, w = [int(s) for s in input().split(' ')]
        if w < w1:
            nlow += c
        elif w == w1:
            nsame += c
        else:
            nhigh += c
    print(f'k={k} ', nlow, nsame, nhigh)
    p = 0
    q = nlow + nsame + nhigh + c1
    # case 1: negative one heavier
    p0 = nhigh
    q0 = q
        # 1- C(k,p0) / C(k, q0)
    # case 2: b1 only left + one or more same at right
        # only calculate when nsame > 0
        # 1


    print('Case #{}: {}'.format(t, ans))
