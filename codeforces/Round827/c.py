# author: mofhu@github
# C. Stripes

t = int(input())

for ncase in range(1, t+1):
    s = input()
    s = []
    for i in range(8):
        s.append(input())
    for i in range(8):
        if s[i] == 'RRRRRRRR':
            ans = 'R'
            break
    else:
        ans = 'B'

    print(ans)


