# author: mofhu@github
# Problem A1: Perfectly Balanced - Chapter 1

ncase = int(input())

a = 'abcdefghijklmnopqrstuvwxyz'

for t in range(1, ncase + 1):
    s = input()
    q = int(input())
    ans = 0
    di = {}
    d00 = {alpha: 0 for alpha in a}
    di = {0:d00}
    for i in range(1,len(s)+1):
        d00 = d00.copy()
        char = s[i-1]
        d00[char] += 1
        di[i] = d00.copy()
    for i in range(q):
        n, k = [int(s) for s in input().split(' ')]
        sq = s[n-1:k]
        # print(sq)
        if k - n % 2 == 0:
            continue
        else:
            d = {alpha: 0 for alpha in a}
            for char in a:
                d[char] = di[k][char] - di[n-1][char]
            # count 26
            flag = 0
            flag_char = 0
            # need a link to char?
            # print('n, k , d', k, n, d)  # debug
            # print(di[n-1])  # debug
            # print(di[k])  # debug
            for char in d:
                if flag == -1:
                    break
                if d[char] % 2 != 0:
                    if flag == 1:
                        flag = -1
                    else:
                        flag = 1
                        flag_char = char
            if flag == -1 or flag == 0:  # not possible
                continue
            else:
                # first half
                d[flag_char] -= 1
                d0 = {alpha: 0 for alpha in a}
                # print(len(sq), sq[:int(len(sq)/2)])
                # for char in sq[:int(len(sq)/2)]:
                #    d0[char] += 1
                # print(sq)
                # print('old', d0)
                for char in a:
                    d0[char] = di[n+int(len(sq)/2)-1][char] - di[n-1][char]
                # print('new',d0)
                # judge flag char in first string
                for alpha in a:
                    if d0[alpha] * 2 != d[alpha]:
                        break  # not right ?
                else:
                    # print(i, sq, 'd0', sq[:int(len(sq)/2)])
                    ans += 1
                    '''
                    print('sq, ' ,sq)
                    print('d', d)
                    for k in d:
                        if d[k] != 0:
                            print(k, d[k])
                    print('d0',d0)
                    for k in d0:
                        if d0[k] != 0:
                            print(k, d0[k])
                    '''
                    continue
                d1 = {alpha: 0 for alpha in a}
                # print('d1',sq[int(len(sq)/2)+1:])
                # for char in sq[int(len(sq)/2)+1:]:
                #     d1[char] += 1
                # print(sq)
                # print('old-d1', d1)
                # judge flag char in first string
                for char in a:
                    d1[char] = di[k][char] - di[n+int(len(sq)/2)][char]
                # print('new', d1)
                for alpha in a:
                    if d1[alpha] * 2 != d[alpha]:
                        # print('d', 'd1', alpha, d[alpha], d1[alpha])
                        break  # not right ?
                else:
                    # print(i, sq, 'd1', sq[int(len(sq)/2)+1:])
                    ans += 1
                    # print('d1')
                    continue


    print('Case #{}: {}'.format(t, ans))
