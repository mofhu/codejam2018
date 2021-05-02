ncase = int(input())

quat = {
    "1i": "i", "1j": "j", "1k": "k",
    "ii": "-1", "ij": "k", "ik": "-j",
    "ji": "-k", "jj": "-1", "jk": "i",
    "ki": "j", "kj": "-i", "kk": "-1"
}

for n in range(1, ncase+1):
    l, x = [int(s) for s in input().split(" ")]
    s = input()  # string
    # print(n, l, x, s)
    s = s * x
    l = l * x
    # print(l, s)

    i = 0
    result = "1"
    target = "i"
    flag = 0
    positive = 1
    while i < l:
        result = quat[result + s[i]]
        if result[0] is "-":
            positive = 0 - positive
            result = result[1]
        if result == target:
            # if l < 100:
            #     print(i, s[i+1:])
            if target is "i" and positive is 1:
                flag += 1
                result = "1"
                target = "j"
            elif target is "j" and positive is 1:
                flag += 1
                result = "1"
                target = "k"
            elif positive is 1:
                flag += 1
                result = "1"
                target = "1"
        i += 1
    # print(flag, result, target)
    if result != "1" or flag < 3 or positive is -1:
        print("Case #{}: NO".format(n))
    else:
        print("Case #{}: YES".format(n))
