# code in python 2

ncase = int(input())


for case in range(1, ncase+1):
    n = int(input())
    s = []
    for d in str(raw_input()):
        s.append(int(d))

    d = int(round((n-0.1)/2, 0))
    if n % 2 == 0:
        t = sum(s[:d])
    else:
        t = sum(s[:d])
    # print(t)
    ans = t
    for i in range(d):
        # print(n, n-1-i, i, len(s))
        ti = t + s[n-1-i] - s[d-1-i]
        t = ti
        if ti < ans:
            ans = ti
    # print(sum(s), ans)
        # print(s[0], s[-1])
    ans = sum(s)-ans
    print("Case #{}: {}".format(case, ans))

