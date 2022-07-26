ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = [i for i in input().split(' ')]
    ans = 0
    for i in range(n-1):
        if int(s[i]) < int(s[i+1]):
            continue
        else:
            if len(s[i]) == len(s[i+1]):
                ans += 1
                s[i+1] = s[i+1] + '0'
            else:
                if int(s[i][:len(s[i+1])]) < int(s[i+1][:len(s[i+1])]):
                    ans += len(s[i]) - len(s[i+1])
                    s[i+1] = s[i+1] + '0' * (len(s[i]) - len(s[i+1]))
                elif int(s[i][:len(s[i+1])]) > int(s[i+1][:len(s[i+1])]):
                    ans += len(s[i]) - len(s[i+1]) + 1
                    s[i+1] = s[i+1] + '0' * (len(s[i]) - len(s[i+1]) + 1)
                else:
                    if int(s[i][len(s[i+1]):]) != int('9'*(len(s[i]) - len(s[i+1]))):
                        ans += len(s[i]) - len(s[i+1])
                        s[i+1] = str(int(s[i]) + 1)
                    else:
                        ans += len(s[i]) - len(s[i+1]) + 1
                        s[i+1] = s[i+1] + '0' * (len(s[i]) - len(s[i+1]) + 1)

    print("Case #{}: {}".format(case, ans))


