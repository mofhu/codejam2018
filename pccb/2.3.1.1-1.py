# author: mofhu@github
# 01 bag example

n = 4
wv = [
    (2,3),
    (1,2),
    (3,4),
    (2,2)
]
W = 5

def rec(i, w):  # version 1: all in function, not preferred.
    print('iwv', i, w)
    if i == n:
        return 0
    wi, vi = wv[i]
    if w-wi >= 0:
        return max(rec(i+1, w-wi)+vi, rec(i+1, w))
    else:
        return rec(i+1, w)

print(rec(0, 5 ))
