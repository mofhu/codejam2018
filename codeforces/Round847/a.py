# author: mofhu@github
# A. Polycarp and the Day of Pi

t = int(input())
s0 = '314159265358979323846264338327'

for ncase in range(1, t+1):
    s = input()
    ans = 0
    i = 0
    while i < len(s) and s[i] == s0[i]:
        ans += 1
        i += 1
    print(ans)




