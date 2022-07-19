# author: mofhu@github
# Count the ACs

t = int(input())
for i in range(t):
    p = input()
    if len(p) == 3:  # >100
        corr = int(p[0]) + int(p[1:])
    elif len(p) == 4:  # 1000
        corr = 10
    else:
        corr = int(p)

    if corr <= 10:
        ans = corr
    else:
        ans = -1
    print(ans)
