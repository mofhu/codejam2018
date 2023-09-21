# author: mofhu@github
# A - Short Sort

t = int(input())

for ncase in range(1, t+1):
    s = input()
    ans = 0
    if s[0] == 'a':
        ans += 1
    if s[1] == 'b':
        ans += 1
    if s[2] == 'c':
        ans += 1
    if ans == 3 or ans == 1:
        print('YES')
    else:
        print('NO')




