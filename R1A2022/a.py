# author: mofhu@github
# Double or One Thing

ncase = int(input())

for case in range(1, ncase+1):
    s = input()
    a = s[0]
    ans = ''
    for i in range(1, len(s)):
        b = s[i]
        if b == a[0]:
            a += b
        elif b > a[0]:
            ans += a + a
            a = b
        else:
            ans += a
            a = b
    ans += a
    print(f'Case #{case}: {ans}')
