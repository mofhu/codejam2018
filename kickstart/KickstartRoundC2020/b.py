ncase = int(input())

t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for case in range(1, ncase+1):
    d = {}
    r, c = [int(s) for s in input().split(" ")]
    s = []
    for i in range(r):
        t = input()
        s.append(t)
        for j in t:
            d[j] = []
    # print(d)
    for i in range(c):
        ci = [s[j][i] for j in range(r-1, -1, -1)]
        char0 = ci[0]
        for char in range(1, len(ci)):
            if ci[char] != char0:
                if char0 not in d[ci[char]]:
                    d[ci[char]].append(char0)
                char0 = ci[char]
    # print(d)
    used = []
    lu = 0
    while True:
        # print(used)
        for key in d:
            if key not in used:
                dk = d[key]
                for j in dk:
                    if j not in used:
                        break
                else:
                    used.append(key)
        if len(used) == len(d):
            ans = ''.join(used)
            break
        elif len(used) == lu:
            ans = -1
            break
        else:
            lu = len(used)

    print("Case #{}: {}".format(case, ans))

