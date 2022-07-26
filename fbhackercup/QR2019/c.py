ncase = int(input())

for i in range(1, ncase+1):
    line = input()

    def and_op(a, b):
        if a == '1' and b == '1':
            return '1'
        else:
            return '0'
    def or_op(a, b):
        if a == '1' or b == '1':
            return '1'
        else:
            return '0'
    def xor_op(a, b):
        if (a == '1'and b == '0') or (b == '1' and a == '0'):
            return '1'
        else:
            return '0'
    def cal(t):
        if t[1] == '|':
            return or_op(t[0], t[2])
        elif t[1] == '&':
            return and_op(t[0], t[2])
        elif t[1] == '^':
            return xor_op(t[0], t[2])

    from collections import deque

    x = 1
    s = deque()  # use as a stack
    if len(line) == 1:
        char = line[0]
        if char == '0' or char == '1':
            ans = 0
        else:
            ans = 1
    else:
        for char in line:
            if char =='(':
                s.append('')
            elif char == ')':
                t = s.pop()
                t1 = cal(t)
                if len(s) == 0:
                    s.append(t1)
                else:
                    t0 = s.pop()
                    # print(t0, t1)
                    s.append(t0 + t1)
            elif char == '0' or char == '1':
                t = s.pop()
                t1 = t + char
                s.append(t1)
            elif char == '|' or char == '&' or char == '^':
                t = s.pop()
                t1 = t + char
                s.append(t1)
            else:  # char == 'x' or 'X'
                if char == 'x':
                    char = '1'
                else:
                    char = '0'
                t = s.pop()
                t1 = t + char
                s.append(t1)
        s1 = s.pop()
        # x = 0
        s = deque()  # use as a stack
        for char in line:
            if char =='(':
                s.append('')
            elif char == ')':
                t = s.pop()
                t1 = cal(t)
                if len(s) == 0:
                    s.append(t1)
                else:
                    t0 = s.pop()
                    # print(t0, t1)
                    s.append(t0 + t1)
            elif char == '0' or char == '1':
                t = s.pop()
                t1 = t + char
                s.append(t1)
            elif char == '|' or char == '&' or char == '^':
                t = s.pop()
                t1 = t + char
                s.append(t1)
            else:  # char == 'x' or 'X'
                if char == 'x':
                    char = '0'
                else:
                    char = '1'
                t = s.pop()
                t1 = t + char
                s.append(t1)
        s2 = s.pop()
        if s1 == s2:
            ans = 0
        else:
            ans = 1

    print('Case #{}: {}'.format(i, ans))
