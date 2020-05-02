# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    n, d = [int(s) for s in input().split(' ')]
    s = [int(i) for i in input().split(' ')]
    s.sort()
    # print(s)
    if d == 2:
        ans = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                ans = 0
                break
    else:
        ans = 2
        for i in range(len(s)-2):
            if s[i] == s[i+1] and s[i+1] == s[i+2]:
                ans = 0
                break
        if ans == 2:
            for i in range(len(s)-1):
                for j in range(i+1, len(s)):
                    if s[i] * 2 == s[j]:
                        ans = 1
                        break
        if ans == 2:
            for i in range(len(s)-2):
                if s[i] == s[i+1]:
                    ans = 1
                    break

    print("Case #{}: {}".format(case, ans))

