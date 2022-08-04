# author: mofhu@github
# B. Permutation Chain

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    print(n)
    a = [str(i) for i in range(1, n+1)]
    print(' '.join(a))
    i = 0
    for i in range(n-1):
        a[i], a[i+1] = a[i+1], a[i]
        print(' '.join(a))


