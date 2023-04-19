# author: mofhu@github
# Untie

ncase = int(input())

for case in range(1, ncase+1):
    s = input()
    ans = 0
    # sort s to simplify edge conditions:
    # make first and last element not the same (except full same sequence)
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            s1 = s[i+1:] + s[:i+1]
            s = s1
            break
    # print(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            ans += 1
            i += 2
        else:
            i += 1
    if s[-1] == s[0]:  # full same
        if len(s) % 2 == 1:
            ans += 1

    print("Case #{}: {}".format(case, ans))
