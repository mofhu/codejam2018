# author: mofhu@github
# A. Deterministic Scheduling for Extended Reality over 5G and Beyond

# earliest attempt:
"""
20231127 design quick mvp

(as target is to maximize # of transferred frames.)
just give each frame a score and try to set from highest to lowest.

may extend other parameters into score functions in later version.
e.g. less power; user/freq...

"""
from math import log2
# debug = True
debug = False
# input
N = int(input())
K = int(input())
T = int(input())
R = int(input())
sinr = []
for i in range(R*K*T):
    line = [float(s) for s in input().split(' ')]
    sinr.append(line)
d = []
for i in range(N*R*K):
    line = [float(s) for s in input().split(' ')]
    d.append(line)
J = int(input())
frames = []
for i in range(J):
    line = [int(s) for s in input().split(' ')]
    frames.append(line)

# print(sinr)
# print(d)
# print(frames)

# output
# k_limit = [[0 for n in range(N)]] * R * T  # not implemented in MVP
p_limit = [min(R, 4) for i in range(T)]  # temp use 4 as max power
# p_limit = [R for i in range(T)]
output = []
for i in range(R*K*T):
    output.append([0 for i in range(N)][:])
# print(output)
if debug:
    print(p_limit)
frames.sort(key=lambda x: x[1]/x[4])


for f in frames:
    if debug:
        print(f[0], p_limit)
    tbs, user, t0 = f[1], f[2], f[3]
    for t in range(t0, t0+f[4]):
        # check if p_limit[t] is still available
        if p_limit[t] <= 0:
            continue
    best_k = {}
    # best_p = {}
    for t in range(t0, t0+f[4]):
        # find best cell (k) for this frame (t)
        if debug:
            print(f'tbs={tbs}, t={t}')
        if p_limit[t] > 0 and tbs > 0:
            for r in range(R):
                # r*k search not implemented in MVP;
                # only find best k in r*k space and use it for all time
                for k in range(K):
                    best_sinr = 0
                    sinr_t_k = sinr[r + k*R + t*K*R -1][user]  # user = f[2]
                    if sinr_t_k > best_sinr:
                        best_sinr = sinr_t_k
                        best_k[t] = k
            if debug:
                print(f't={t}, best_k is {best_k[t]}, best_sinr is {best_sinr}')
                print(f'bestk {best_k}')
            best_p = min(p_limit[t], 4)
            if best_p > 0:
                p_limit[t] -= best_p
                # print(f'frame{f[0]}, user{f[2]}, best_sinr {best_sinr}, best_p: {best_p[t]}')  # debug
                # ignore the calculation of transferred bits in MVP
            gt = 192 * log2(1 + best_sinr*best_p)
            tbs -= gt
            # set best_k to output
            if t in best_k:
                k = best_k[t]
                output[r + k*R + t*K*R -1][user] = best_p
if debug:
    print(p_limit)
# print(output)  # debug
for i in output:
    print(' '.join(map(str, i)))
