# author: mofhu@github
# Complementary Strand in a DNA

t = int(input())
for i in range(t):
    x = int(input())
    s = input()
    ans = ''
    comp = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    for c in s:
        ans += comp[c]
    print(ans)
