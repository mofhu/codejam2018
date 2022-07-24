ncase = int(input())

for case in range(1, ncase+1):
    n, k = [int(s) for s in input().split(" ")]
    u = float(input())
    pi = [float(s) for s in input().split(" ")]
    pi.sort()
    # print(pi)

    sum_pi = sum(pi[n-k:])
    total = sum_pi + u
    ave = total / k
    # print(k, u, sum_pi)

    # cal final p
    q = 0
    if u - k + sum_pi > -1e-8:
        q = 1
    else:
        used = 0
        i = int(n - k)
        eq = 1
        # print(pi)
        while u - used > -1e-8:
            # print(i, pi, u-used)
            if i < n-1:
                delta = pi[i+1] - pi[i]
            if i < n-1 and u - used > delta * eq:
                for j in range(i+1):
                    pi[j] = pi[i+1]
                used += delta * eq
                eq += 1
                i += 1
            else:
                ave_inc = (u-used) / eq
                # print(i)
                for j in range(n-k, i+1):
                    pi[j] += ave_inc
                break

    s = []
    def gen(n, k, init_i, init_s):
        # print(n, k, init_i, init_s)
        i = init_i
        # print(i, n-k)
        if i < n:
            if len(init_s) + 1 == k:
                s.append(init_s[:] + [i])
            else:
                gen(n, k, i+1, init_s[:]+[i])
            gen(n, k, i+1, init_s[:])
    # gen(30,10,0,[])
    # print(len(s))

    # print(pi)
    if q != 1:
        if n == k:
            q = 1
            for j in pi:
                q *= j
        else:
            q = 1
            gen(n,k,0,[])
            for i in s:
                q0 = 1
                for j in i:
                    q0 *= pi[j]
                q *= 1-q0
            q = 1-q


    print("Case #{}: {:.8f}".format(case, q))

