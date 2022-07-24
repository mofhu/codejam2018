ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = []
    ans_front = []
    ans_end = []
    for i in range(n):
        s.append(input())
        # print(t)
    s.sort()
    # print(s)
    flag = True
    pass_front = False
    pass_end = False
    while(flag and len(s) > 0):
        # print(ans_front, ans_end)
        # print(s)
        # front cycle
        to_clean_front = []
        to_clean_end = []
        if not pass_front:
            front = "*"
            to_clean_front = []
            for i in range(len(s)):
                if s[i][0] != "*":
                    if front != "*" and front != s[i][0]:
                        flag = False
                        break
                    else:
                        front = s[i][0]
                        to_clean_front.append(i)
            # print(front)
            if front == "*":
                pass_front = True
            else:
                ans_front.append(front)
        # end cycle
        to_clean_end = []
        if not pass_end:
            end = "*"
            for i in range(len(s)):
                # print(s[i])
                if s[i][-1] != "*":
                    if end != "*" and end != s[i][-1]:
                        flag = False
                        break
                    else:
                        end = s[i][-1]
                        to_clean_end.append(i)
            if end == "*":
                pass_end = True
            else:
                ans_end.append(end)
        for i in to_clean_end:
            s[i] = s[i][:-1]
        for i in to_clean_front:
            s[i] = s[i][1:]
        # if all pass happens
        if pass_front and pass_end:
            # possible bug from max len here
            max_len = 0
            max_idx = 0
            for i in range(len(s)):
                if len(s[i]) > max_len:
                    max_len = len(s[i])
                    max_idx = i
            if max_len > 2:
                s[max_idx] = s[max_idx][1:-1]
                if len(s[max_idx]) > 1:
                    pass_front = False
                    pass_end = False
                elif len(s[max_idx]) > 0:
                    pass_front = False
            else:
                break
        # clear only *
        for i in range(len(s)-1, -1, -1):
            if s[i] == "*" or s[i] == "":
                del s[i]
        print(s)
    #  ans
    if flag:
        ans_end.reverse()
        ans = "".join(ans_front+ans_end)
        if len(ans) > 10000:
            ans = "*"
    else:
        ans = "*"

    print("Case #{}: {}".format(case, ans))


