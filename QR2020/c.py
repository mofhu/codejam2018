# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    acts = []
    for i in range(n):
        s = [int(s) for s in input().split(' ')]
        acts.append([i, s[0], s[1]])
    acts.sort(key=lambda x:x[1])
    # print(acts)

    tc = 0
    tj = 0
    ans = ''
    for i in range(n):
        ts = acts[i][1]
        te = acts[i][2]
        if ts >= tc:
            acts[i].append('C')
            tc = te
        elif ts >= tj:
            acts[i].append('J')
            tj = te
        else:
            ans = 'IMPOSSIBLE'
            break
    if ans != 'IMPOSSIBLE':
        acts.sort(key=lambda x:x[0])
        for i in range(n):
            ans += acts[i][3]

    print("Case #{}: {}".format(case, ans))

