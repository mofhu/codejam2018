# author: mofhu@github
# C - PC on the Table

h, w = [int(s) for s in input().split(' ')]


for j in range(h):
    s = input()
    s1 = []
    i = 0
    while i <= len(s)-1:
        if i < len(s) - 1 and s[i] == 'T' and s[i+1] == 'T':
            s1.append('PC')
            i += 2
        else:
            s1.append(s[i])
            i += 1
    print(''.join(s1))
