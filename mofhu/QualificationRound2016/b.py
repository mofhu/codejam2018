t = int(input())

for case in range(1, t+1):
    s = input()
    #print(s)
    s = s[::-1]
    #print(s)
    s = list(s)

    n = 0
    for i in range(0, len(s)):
        if s[i] is '-':
            n += 1
            for i in range(i+1, len(s)):
                if s[i] is '-':
                    s[i] = '+'
                else:
                    s[i] = '-'
        #print(s[i])

    print("Case #{}: {}".format(case, n))

