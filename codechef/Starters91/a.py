# author: mofhu@github
# Blobby Volley Scores

t = int(input())
for ncase in range(t):
    n = int(input())
    s = input()
    flag = 'A'
    a, b = 0, 0
    for i in range(n):
        if s[i] == flag:
            if s[i] == 'A':
                a += 1
            else:
                b += 1
        else:
            flag = s[i]
    print(a, b)
