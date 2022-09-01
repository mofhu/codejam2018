# author: mofhu@github
# B. Colourblindness

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s1 = [i for i in input()]
    s2 = [i for i in input()]
    for i in range(n):
        if s1[i] == 'G':
            s1[i] = 'B'
        if s2[i] == 'G':
            s2[i] = 'B'
        if s1[i] != s2[i]:
            # print(i, s1[i], s2[i])
            ans = 'NO'
            break
    else:
        ans = 'YES'
    print(ans)


