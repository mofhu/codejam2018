# author: mofhu@github
# Odd GCD Permutation

t = int(input())
for ncase in range(t):
    n = int(input())
    if n % 2 == 1:
        ans = -1
    else:
        ans = ' '.join([str(i) for i in range(n,0,-1)])

    print(ans)
