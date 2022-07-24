# author: mofhu@github

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    d0 = []
    for i in range(n):
        s = input()
        t = [s1 for s1 in s]
        t.reverse()
        d0.append("".join(t))
    # print(d0)

    ldic = {}
    for i in range(51):
        ldic[i] = []
    dic = {}
    for word in d0:
        for i in range(len(word)):
            rhy = word[:i+1]
            if rhy not in dic:
                ldic[i].append([rhy, 1])
                dic[rhy] = [word]
            else:
                dic[rhy].append(word)
                for rh in ldic[i]:
                    if rh[0] == rhy:
                        rh[1] += 1
    # print(dic)
    # print(ldic)
    ans = 0
    i = 50
    used = []
    while(i >= 0 and ans < n):
        if len(ldic[i]) > 0:
            # print(ldic[i])
            for rhy in ldic[i]:
                if rhy[1] >= 2:
                    # print(i, rhy, dic[rhy[0]])
                    dw = []
                    for w in dic[rhy[0]]:
                        # print(w)
                        if w not in used:
                            dw.append(w)
                    # print("dw",dw)
                    if len(dw) >= 2:
                        j = 0
                        # print("used", used)
                        while j < len(dw):
                            used.append(dw[j])
                            used.append(dw[j+1])
                            j += 2
                            break
                        # print("used", used)



        i -= 1




    ans = len(used)

    print("Case #{}: {}".format(case, str(ans)))

