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
#debug = True
debug = False
MIN_THRESHOD = 0.0000000001

from math import log2
import math
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

# output
# k_limit = [[0 for n in range(N)]] * R * T  # not implemented in MVP
gp_limit = [R for i in range(T)]  # global power limit
p_limit = [min(R, 4) for i in range(T)]  # temp use 4 as max power
b_limit = [-1 for i in range(T)]  # bool limit for r*k, will be set to user id if used 

output = []
for i in range(R*K*T):
    output.append([0 for i in range(N)][:])

frames.sort(key=lambda x: x[1]/x[4])


for f in frames:
    # print(p_limit)
    if debug:
        print(f'before frame #{f[0]}')
        print(output)
        print(f'frame #{f[0]}\n', p_limit)
    tbs, user, t0 = f[1], f[2], f[3]
    best_kp = {}  # best_kp[t] {t: [best_kp@t, p: best_p@t]}
    all_t_kp ={}  # all_t_kp[t] {t: [k, p, gt]}
    # note: time-first or freq-first search may have different results...optimize later if possible
    tkp = {}  # tkp[t] {t: [k, p, gt]}, will sort later by gt-descending
    flag_transfer = False  # if can be transferred
    for t in range(t0, t0+f[4]):
        # check if p_limit[t] is still available
        if p_limit[t] - min(R, 4) > MIN_THRESHOD or gp_limit[t] - R > MIN_THRESHOD: # or b_limit[t]:
            if debug:
                print(f'used power here for frame #{f[0]} at t={t}')
            # no way to use more power here
            continue
        if b_limit[t] != -1:
            user_m = b_limit[t]
            dmrn = d[user_m + r*N + k*R*N][user]
            # print(f'dmrn ={dmrn}, user_m={user_m}, r={r}, k={k}')
            if dmrn < 0:
                continue
        # find best cell (k) for this frame (t)
        if debug:
            print(f'tbs={tbs}, t={t}')
        if p_limit[t] > MIN_THRESHOD and gp_limit[t] > MIN_THRESHOD:
            if b_limit[t] != -1:  # can transfer            
                user_m = b_limit[t]
                dmrn = d[user_m + r*N + k*R*N][user]
                print(f'dmrn ={dmrn}, user_m={user_m}, r={r}, k={k}')
                if dmrn < 0:
                    continue
            all_t_kp[t] = []
            for r in range(R):
                # r*k search not implemented in MVP;
                # only find best k in r*k space and use it for all time
                for k in range(K):
                    best_sinr = 0
                    sinr_t_k = sinr[r + k*R + t*K*R -1][user]  # user = f[2]
                    all_t_kp[t].append((r, k, sinr_t_k))  # all_t_kp[t] {t: [k, p, gt]}
                    
                    if sinr_t_k > best_sinr:
                        best_sinr = sinr_t_k
                        best_kp[t] = [k, 0]
            if debug:
                print(f't={t}, best_kp is {best_kp[t]}, best_sinr is {best_sinr}')
                print(f'bestk {best_kp}')
            
            best_p = min(p_limit[t], gp_limit[t], 4)
            gt = 192 * log2(1 + best_sinr*best_p)

            tkp[t] = [best_kp[t][0], best_p, gt]
            if debug:
                print(f't={t}, best_kp is {best_kp[t]}, best_sinr is {best_sinr}')
                print(f'tbs={tbs}, gt={gt}, best_p={best_p}')
                
    # print(f'tkp={tkp}')
    # print(f'all_t_kp={all_t_kp}')
    # find if can transfer
    if len(tkp) > 0:
        output_rkt = []  # output for r*k: (r, k, t, p)
        tkp = sorted(tkp.items(), key=lambda x: x[1][2], reverse=True)
        # print(all_t_kp)
        # print(tkp)
        if debug:
            print(f'tkp={tkp}')
        for t0 in tkp:  # find best t to use here
            if flag_transfer:
                break
            ti, gt = t0[0], t0[1][2]
            #print(f't={ti}, iteration begins at {ti}, remaining tbs={tbs}')
            #print(f't={ti}', all_t_kp[ti])
            alltkp = sorted(all_t_kp[ti], key=lambda x: x[1], reverse=True)
            # print(f'alltkp @ ti={ti}: {alltkp}')  # debug
            all_gt = 0
            best_sinr_t_k = alltkp[0][2]  # best sinr for this t
            ADD_R = 0.2  # note: temp threshold (to highest sinr) for adding r at the same time
            sinr_r_k = []
            for r, k, sinr_t_k in alltkp:
                if sinr_t_k >= best_sinr_t_k * ADD_R:
                    sinr_r_k.append((r, k, sinr_t_k))
            # prod_sinr_tk = sinr_r_k[0]
            # gmean_sinr_tk = prod_sinr_tk
            # print(f'sinr_r_k: r, k, sinr', sinr_r_k)
            for i in range(len(sinr_r_k)):
                # print(f'i={i}, output_rkt={output_rkt}')
                _r, _k, _sinr = sinr_r_k[i]
                # calculate accumulated sinr for all r*k
                _p = min(p_limit[t], gp_limit[t], 4)
                if i == 0:
                    all_sp = _sinr * _p
                    all_gt = 192 * log2(1 + _sinr * _p)
                    #print(f'_sinr={_sinr}, _p={_p}, all_gt={all_gt}')
                    output_rkt.append((_r, _k, ti, _p))
                else:
                    all_sp *= (_sinr * _p)
                    gmean_sp = all_sp ** (1 / (i+1))
                    all_gt = 192 * log2(1 + gmean_sp) * (i+1)
                    #print(f'i={i},_sinr={_sinr}, _p={_p}, all_gt={all_gt}')
                    output_rkt.append((_r, _k, ti, _p))
                # print('tttttt', tbs, all_gt)
                p_limit[ti] -= _p
                gp_limit[ti] -= _p
                if tbs > all_gt:
                    pass  # continue to add r*k
                    ## best_kp[ti][1] = t0[1][1]
                else:
                    # finished
                    flag_transfer = True
                    # calculate true best_p lower than current
                    ## real_p = (2**(tbs * 1.000001 / 192) -1) / best_sinr

                if p_limit[ti] == 0 or gp_limit[ti] == 0:
                    # no power for this ti anymore.
                    if not flag_transfer:
                        tbs -= all_gt
                    # print(f'tttt={ti}, tbs={tbs}, all_gt={all_gt}')
                    break
    # print(f'output_rkt: r,k,t,p', output_rkt)
    if flag_transfer:
        # only write when transfered (filter not possible frames)
        if debug:
            print(f'frame {f[0]}, best_kp={best_kp} tkp={tkp}')
        for r,k,t,p in output_rkt:
            # k1, p1 = best_kp[t][0], best_kp[t][1]
            p1 = max(p-0.00000001, p*0.99999999)
            if p1 > MIN_THRESHOD:
                if p1 == 3.99999999: p1 = 4
                # p_limit[t] -= p1
                # gp_limit[t] -= p1
                b_limit[t] = user
                output[r + k*R + t*K*R -1][user] = p1
            continue
if debug:
    print(p_limit)
# print(output)  # debug
for i in output:
    print(' '.join(map(str, i)))
