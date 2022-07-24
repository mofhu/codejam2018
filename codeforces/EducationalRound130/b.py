# author: mofhu@github
# B. Promo

n, q = [int(i) for i in input().split(' ')]
p = [int(s) for s in input().split(' ')]
p.sort(reverse=True)
d = {}
for i in range(q):
    x, y = [int(i) for i in input().split(' ')]
    if (x, y) not in d:
        ans = sum(p[x-y:x])
        d[(x,y)] = ans
    else:
        ans = d[(x,y)]
    print("{}".format(ans))


