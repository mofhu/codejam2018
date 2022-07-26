ncase = int(input())

def swap3(n):
    return



for case in range(1, ncase+1):
    n = int(input())
    v = [int(s) for s in input().split(" ")]
    # print(n, v)

    v1 = v[::2]
    v2 = v[1::2]
    # print(v1, v2)
    v1.sort()
    v2.sort()
    # print(v1, v2)
    flag = -1
    for i in range(len(v1)):
        if flag != -1:
            break
        j = i
        if j == len(v2): break
        if v1[i] > v2[j]:
            flag = i+j
            break
        if j < len(v2) - 1:
            if v2[j] > v1[i+1]:
                flag = i+j+1
                break
        else:
            if len(v1) > len(v2):
                if v2[j] > v1[i+1]:
                    flag = i+j+1
                    break
    if flag == -1:
        flag = "OK"
    print("Case #{}: {}".format(case, flag))

