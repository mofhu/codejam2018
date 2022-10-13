# author: mofhu@github
# A. Planets

t = int(input())

for ncase in range(1, t+1):
    seq = {'S':0, 'M':1, 'L':2}
    l, r = [s for s in input().split(' ')]
    if l[-1] == r[-1]:  # compare num X
        if len(l) < len(r):
            if l[-1] == 'S':
                ans = '>'
            else:
                ans = '<'
        elif len(l) > len(r):
            if l[-1] == 'S':
                ans = '<'
            else:
                ans = '>'
        else:
            ans = '='
    else:
        if seq[l[-1]] < seq[r[-1]]:
            ans = '<'
        else:
            ans = '>'
    print(ans)


