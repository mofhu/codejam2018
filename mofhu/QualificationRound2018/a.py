ncase = int(input())

def damage(p):
    count = 0
    shot = 1
    for char in p:
        if char == "C":
            shot *= 2
        else:
            count += shot
    return count

for case in range(1, ncase+1):
    d, p = [s for s in input().split(" ")]
    d = int(d)
    # print(d, p)
    # print(damage(p))
    c, s = p.count("C"), p.count("S")
    # print(c,s)  # count c, count s

    if s > d:
        swap = "IMPOSSIBLE"
    elif damage(p) <= d:
        swap = 0
    else:
        swap = 0
        while (damage(p) > d):
            # print(swap, p, damage(p))
            for i in range(len(p) - 1):
                if p[i] == "C" and p[i+1] == "S":
                    p = list(p)
                    p[i] = "S"
                    p[i+1] = "C"
                    p = "".join(p)
                    swap += 1
                    break

    print("Case #{}: {}".format(case, swap))

