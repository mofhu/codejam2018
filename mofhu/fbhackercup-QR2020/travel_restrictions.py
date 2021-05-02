ncase = int(input())

for case in range(1, ncase + 1):
    n = int(input())
    i = input()
    o = input()
    ans = [['N' for j in range(n)] for k in range(n)]
    # print(i,o, ans)
    for oi in range(n):
        for ii in range(n):
            if oi == ii:
                # print(oi, ii)
                # print(ans[oi][ii])
                ans[oi][ii] = 'Y'
            else:
                if o[oi] == 'Y' and i[ii] =='Y' and abs(oi-ii) == 1:
                    # print(oi, ii)
                    # print(ans[oi][ii])
                    ans[oi][ii] = 'Y'
    for oi in range(n):
        for ii in range(n):
            if abs(oi-ii) > 1:
                if oi > ii:
                    p = oi
                    while p-1 >= ii:
                        if ans[p][p-1] == 'N':
                            break
                        else:
                            p -= 1
                    else:
                        # print(oi, ii)
                        ans[oi][ii] = 'Y'
                elif oi < ii:
                    p = oi
                    while p+1 <= ii:
                        if ans[p][p+1] == 'N':
                            break
                        else:
                            p += 1
                    else:
                        # print(oi, ii)
                        ans[oi][ii] = 'Y'


    print('Case #{}:'.format(case))
    # print(ans)
    for line in ans:
        print(''.join(line))

