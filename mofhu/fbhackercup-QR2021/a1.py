# author: mofhu@github

t = int(input())

for ncase in range(1, t+1):
    # count all letters
    s = input()
    d = {}
    v = {'A', 'E', 'I', 'O', 'U'}
    cv = 0
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        if i in v:
            cv += 1
    cc = len(s) - cv
    ld = [(d[i], i) for i in d]
    ld = sorted(ld, reverse=True)
    #print(ld)
    # find min v&w cases
    flagv = 0
    flagc = 0
    ansv = 3*len(s)
    ansc = 3*len(s)
    if cv == 0 or cc == 0:
        anst = len(s)
    else:
        anst = 3*len(s)
    for c, letter in ld:
        if flagv and flagc: break
        if flagv == 0 and letter in v:
            flagv = 1
            ansv = cc + 2*(cv-c)
        elif flagc == 0 and letter not in v:
            flagc = 1
            ansc = cv + 2*(cc-c)
    # print(ansc, ansv)
    ans = min(ansv, ansc, anst)

    # output
    print('Case #{}: {}'.format(ncase, ans))
