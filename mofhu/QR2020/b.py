# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    s = input()
    s += '0'
    t = 0
    ans = ''
    for i in s:
        inti = int(i)
        if inti > t:
            ans += '(' * (inti-t) + i
        elif inti == t:
            ans += i
        else:
            ans += ')' * (t-inti) + i
        t = inti


    print("Case #{}: {}".format(case, ans[:-1]))


