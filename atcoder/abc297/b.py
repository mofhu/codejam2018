# author: mofhu@github
# B - chess960

s = input()

b = []
r = []
k = []
for i in range(len(s)):
    if s[i] == 'B':
        b.append(i)
    elif s[i] == 'R':
        r.append(i)
    elif s[i] == 'K':
        k.append(i)

if b[0] % 2 + b[1] % 2 == 1 and r[0] < k[0] < r[1]:
    print('Yes')
else:
    print('No')
