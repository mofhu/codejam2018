# author: mofhu@github
# F. Smaller

t = int(input())

for ncase in range(1, t+1):
    q = int(input())
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_rev = alpha[::-1]
    # print(alpha_rev)
    da = {i:0 for i in alpha}
    db = {i:0 for i in alpha}
    da['a'] = 1
    db['a'] = 1

    for i in range(q):
        d, k, x = [s for s in input().split(' ')]
        d = int(d)
        k = int(k)

        dx = {j:0 for j in alpha}
        for j in x:
            dx[j] += 1
        if d == 1:
            for j in alpha:
                da[j] += k * dx[j]
        else:
            for j in alpha:
                db[j] += k * dx[j]

        # compare a/b
        # print(da)
        # print(db)
        for j in alpha_rev[:-1]:
            if db[j] > 0:
                ans = 'YES'
                break
        else:
            for j in alpha_rev:
                if da[j] > db[j]:
                    ans = 'NO'
                    break
            else:
                # print(db['a'], da['a'])
                if db['a'] > da['a']:
                    ans = 'YES'
                else:
                    ans = 'NO'

        print(ans)



