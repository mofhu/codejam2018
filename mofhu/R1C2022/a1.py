# author: mofhu@github
# Pancake Deque

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = [i for i in input().split(' ')]
    alpha = {i:[0,0,0,0] for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    words = {i:[[],[],[],[]] for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    flag_impossible = False
    for word in s:
        if flag_impossible:
            break
        dword = []
        letter = 0
        for i in word:
            if flag_impossible:
                break
            if letter == 0:
                letter = i
                dword.append(i)
            else:
                if i != letter:
                    letter = i
                    if i in dword:  # second
                        flag_impossible = True
                        break
                    dword.append(i)
                if i not in dword:
                    dword.append(i)
        # print(dword, len(dword))
        if len(dword) == 1:  # single letter
            alpha[dword[0]][0] += 1
            words[dword[0]][0].append(word)
        else:
            alpha[dword[0]][1] += 1  # begin
            words[dword[0]][1].append(word)
            alpha[dword[-1]][2] += 1  # end
            for i in range(1, len(dword)-1):
                alpha[dword[i]][3] += 1  # middle

    begin = []
    end = []
    free = []
    for i in alpha:
        if flag_impossible:
            break
        if sum(alpha[i][1:]) > 2:
            flag_impossible = True
            break
        elif alpha[i][3] == 1 and sum(alpha[i][1:]) == 2:
            flag_impossible = True
            break
        elif alpha[i][2] == 2 or alpha[i][3] == 2:
            flag_impossible = True
            break
        if sum(alpha[i]) != 0 and sum(alpha[i]) == alpha[i][0]:
            free.append(i)
        if alpha[i][1] == 1:
            begin.append(i)
        if alpha[i][2] == 1:
            end.append(i)
    # print(free)
    # print(begin)
    # print(end)

    from collections import deque
    t = deque()
    for i in range(len(s)):
        t.append([i])
    # print(t)
    ans = ''
    ansans = ''
    flag_ans = False
    while t:
        if flag_ans:
            break
        idx = t.popleft()
        if len(idx) == n:
            # print(idx)
            ans = ''.join(s[i] for i in idx)
            used_letter = []
            current = 0
            for i in ans:
                if i == current:
                    continue
                elif i in used_letter:
                    flag = False
                    break
                else:
                    used_letter.append(i)
                    current = i
            else:
                # print(ans)
                ansans = ans
                flag_ans = True
        else:
            for i in range(len(s)):
                if i not in idx:
                    t.appendleft(idx+[i])

    if not flag_ans:
        ansans = "IMPOSSIBLE"
    print(f'Case #{case}: {ansans}')
