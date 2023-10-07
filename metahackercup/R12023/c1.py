# author: mofhu@github
# C1: Back in Black (Chapter 1)

ncase = int(input())

def button(s, n, i):
    j = i - 1
    while j < n:
        if (j+1) % i == 0:
            s[j] = 1-s[j]
        j += i
    return s

for t in range(1, ncase + 1):
    n = int(input())
    s = [int(i) for i in input()]
    q = int(input())
    b = {}
    for j in range(q):
        i = int(input())
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
    # print('s0', s)
    # print(b)
    for i in b:
        if b[i] % 2 != 0:
            s = button(s, n, i)
    # print('s1', s)
    ans = 0
    for i in range(1,n+1):
        if s[i-1] == 1:
            ans += 1
            # print(f's0@{i}',s)
            s = button(s, n, i)
            # print(f's1@{i}',s)

    print('Case #{}: {}'.format(t, ans))

