# author: mofhu@github
# C1: Second Meaning

ncase = int(input())

for t in range(1, ncase + 1):
    n = int(input())
    c1 = input()
    c = []
    if len(c1) >= 7:  # must have enough space for equal length
        for i in range(n):
            ci = str(bin(i))[2:]
            # print('ci', ci)
            ci = '0' * (len(c1) - len(ci)) + ci
            code_ci = ''
            for j in ci:
                if j == '0':
                    code_ci += '.'
                else:
                    code_ci += '-'
            if code_ci != c1:
                c.append(code_ci)
            else:
                pass
                # print('debug', code_ci)
            if len(c) == n-1:
                break
    else:
        # make len(ci) = 199 (is a prime)
        c1_comp = ''
        for i in c1:
            if i == '.':
                c1_comp += '-'
            else:
                c1_comp += '.'
        # print(c1_comp)
        for i in range(n-1):
            ci = str(bin(i))[2:]
            # print('ci', ci)
            ci = '0' * (199-len(c1)-len(ci)) + ci
            # print(ci)
            code_ci = ''
            for j in ci:
                if j == '0':
                    code_ci += '.'
                else:
                    code_ci += '-'
            c.append(c1_comp + code_ci)

    # print(c)
    print('Case #{}:'.format(t))
    for i in c:
        print(i)
        # print('debug len ci = {}'.format(len(i)))

