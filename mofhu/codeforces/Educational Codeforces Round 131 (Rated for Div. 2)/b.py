# author: mofhu@github
# B. Permutation

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    d = 2
    print(f'{d}')
    ans = ''
    s = [i for i in range(1, n+1)]
    s1 = []
    for i in range(1, n+1, 2):
        s0 = i
        if s[0] > n / 2 + 2:
            s1 += [str(i) for i in range(i, n+1, 2)]
            break
        t = [s0]
        while s0 * 2 <= n:
            s0 *= 2
            t.append(s0)
        s1 += [str(i) for i in t]
    print(' '.join(s1))


