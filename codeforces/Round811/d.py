# author: mofhu@github
# D. Color with Occurrences

t = int(input())

# import re
for ncase in range(1, t+1):
    text = input()
    n = int(input())
    s = []
    idx = {i:[] for i in range(len(text))}
    for i in range(n):
        si = input()
        s.append(si)
        # print(re.finditer(si, text))
        for j in range(len(text)-len(si)+1):
            # print(j, text[j:j+len(si)], si)
            if text[j:j+len(si)] == si:
                for k in range(j, j+len(si)):
                    idx[k].append((j+len(si), i+1, j+1))
    # print(idx)
    for k in idx:
        idx[k].sort(reverse=True)
    i = 0
    ans = []
    while i < len(text):
        if len(idx[i]) == 0:
            ans = -1
            print(ans)
            break
        else:
            news = idx[i][0]
            i = news[0]
            ans.append((news[1], news[2]))
    else:
        print(len(ans))
        for i in ans:
            print(i[0], i[1])


