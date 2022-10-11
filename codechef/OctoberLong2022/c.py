# author: mofhu@github
# Single Operation Part 2

t = int(input())
for ncase in range(t):
    n = int(input())
    s = input()
    f0 = 0
    for i in range(1,len(s)):
        if s[i] == '1':
            f0 = i
            break
    else:
        f0 = n
    ans = f0

    print(ans)

