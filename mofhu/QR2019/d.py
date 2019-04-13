ncase = int(input())

mods = {}
gmod2 = "01" * 520
mods[2]=gmod2
gmod4 = "0011" * 260
mods[4]=gmod4
gmod8 = "00001111" * 150
mods[8]=gmod8
gmod16 = ("0"*8+"1"*8) * 100
mods[16]=gmod16
gmod32 = ("0"*16+"1"*16) * 40
mods[32]=gmod32
gmod64 = ("0"*64+"1"*64) * 15
mods[64]=gmod64
gmod128 = ("0"*128+"1"*128) * 5
mods[128]=gmod128
gmod256 = ("0"*256+"1"*256) * 3
mods[256]=gmod256
gmod512 = "0"*512+"1"*512
mods[512]=gmod512
# print(mods)

import time

for case in range(1, ncase+1):
    # print(case)
    time.sleep(0.1)
    n, b, f = [int(s) for s in input().split(" ")]
    # print(len(guess))
    ans = {}
    for i in mods:
        print(mods[i][:n])
        time.sleep(0.1)
        res = input()
        time.sleep(0.1)
        ans[i] = res

    ids = []
    for i in range(n-b):
        idx = 0
        for key in ans:
            idx += int(key * int(ans[key][i]) / 2)
        ids.append(idx)
    # print("ids", ids)

    ans = []
    for i in range(n):
        if i not in ids:
            ans.append(str(i))
    print(" ".join(ans))

    time.sleep(0.1)

    res = input()
    time.sleep(0.1)
    if res == "1":
        continue
    else:
        break

    time.sleep(0.1)
