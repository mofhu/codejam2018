# author: mofhu@github
# B1: Sum 41 (Chapter 1)

ncase = int(input())

p41 = [2,3,5,7,11,13,17,19,23,29,31,37,41]

for t in range(1, ncase + 1):
    n = int(input())
    ans = -1
    a = []
    for i in p41:
        while n % i == 0:
            a.append(i)
            n = n / i
    if n == 1 and sum(a) <= 41:
        if sum(a) < 41:
            a += [1 for i in range(41-sum(a))]
        ans = len(a)
        print('Case #{}: {} {}'.format(t, ans, ' '.join([str(i) for i in a])))
    else:
        ans = -1
        print('Case #{}: {}'.format(t, ans))

