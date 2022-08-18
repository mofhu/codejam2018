# author: mofhu@github
# A - Full House

s = [int(s) for s in input().split(' ')]
s.sort()

if s[0] == s[2]:
    if s[3] == s[4]:
        print('Yes')
    else:
        print('No')
elif s[2] == s[4]:
    if s[0] == s[1]:
        print('Yes')
    else:
        print('No')
else:
    print('No')
