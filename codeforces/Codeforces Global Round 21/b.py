# author: mofhu@github
# B. NIT Destroys the Universe

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    a = [int(s) for s in input().split(' ')]
    ans = 0
    flag0 = True
    for i in range(n):
        if a[i] == 0:
            if flag0 == True:
                pass
            else:
                flag0 = True
        else:
            if flag0 == True:
                flag0 = False
                ans += 1
            else:
                pass
    if ans > 2:
        ans = 2
    print(f'{ans}')
