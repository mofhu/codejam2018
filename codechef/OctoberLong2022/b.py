# author: mofhu@github
# Single Operation Part 1

t = int(input())
for ncase in range(t):
    n = int(input())
    s = input()
    f0 = 0
    for i in range(len(s)):
        if s[i] == '0':
            f0 = i
            break
    else:
        f0 = n
    ans = f0

    print(ans)
