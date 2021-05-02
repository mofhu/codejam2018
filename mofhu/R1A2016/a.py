ncase = int(input())

for case in range(1, ncase+1):
    s = input()

    ans = [s[0]]
    i = 1
    while(i < len(s)):
        new = s[i]
        # print([s[i]], ans)
        sbegin = "".join([s[i]] + ans)
        send = "".join(ans + [s[i]])
        if sbegin > send:
            ans = [sbegin]
        else:
            ans = [send]
        i += 1
    print("Case #{}: {}".format(case, ans[0]))

