# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    s = int(input())
    ans = ""
    if s <= 3:
        for i in range(s):
            ans += "{} 1\n".format(i+1)
    else:
        for i in range(2):
            ans += "{} 1\n".format(i+1)
        i = 2
        t = 2
        while t < s:
            if t + i <= s:
                new = "{} 2\n".format(i+1)
                ans += new
                t = t + i
                i += 1
            else:
                break
        if t < s:
            t += 1
            new = "{} 1\n".format(i)
            ans += new
            while t < s:
                new = "{} 1\n".format(i+1)
                ans += new
                i += 1
                t += 1


    print("Case #{}:".format(case))
    print("{}".format(ans[:-1]))

