# author: mofhu@github
# A. Spell Check

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s = [i for i in input()]
    s.sort()
    if ''.join(s) == 'Timru':
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)

