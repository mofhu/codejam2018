# author: mofhu@github
# B. Three Threadlets

t = int(input())

for ncase in range(1, t+1):
    s = [int(s) for s in input().split(' ')]
    s.sort()

    for i in range(4):
        if s[0] == s[-1]:
            ans = 'YES'
            break
        else:
            s.append(s[-1]-s[0])
            s[-2] = s[0]
            s.sort()
            # print(s)
    else:
        ans = 'NO'


    print(ans)


