# author: mofhu@github
# C. Word on the Paper

t = int(input())

for ncase in range(1, t+1):
    s = ['' for i in range(8)]
    for i in range(8):
        a = input()
        for j in range(8):
            s[j] += a[j]
    # print(s)
    for i in range(8):
        if s[i] != '........':
            ans = ''
            for j in s[i]:
                if j != '.':
                    ans += j
    print(ans)


