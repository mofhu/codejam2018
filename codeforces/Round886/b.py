# author: mofhu@github
# B. Ten Words of Wisdom

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    ans = 0
    b = 0
    i = 1
    while i < n+1:
        ai, bi = [int(s) for s in input().split(' ')]
        if ai <= 10:
            if bi > b:
                ans = i
                b = bi
        i += 1

    print(ans)


