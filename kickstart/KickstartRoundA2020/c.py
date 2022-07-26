ncase = int(input())
from math import ceil

for case in range(1, ncase+1):
    n, k = (int(s) for s in input().split(' '))
    mi = [int(s) for s in input().split(' ')]
    # diff mi
    dmi = [mi[i+1] - mi[i] for i in range(0, len(mi)-1)]
    dmi.sort(reverse=True)
    # print(dmi)
    filtered = [i for i in dmi if i>1]
    # print(filtered)
    t = 1
    if len(filtered) >= 2 and k == 1:
        t = max(filtered[1], ceil(filtered[0] / 2))
    elif len(filtered) == 1 and k == 1:
        t = max(1, ceil(filtered[0] / 2))


    print("Case #{}: {}".format(case, t))

