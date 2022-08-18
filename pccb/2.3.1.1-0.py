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

def rec(i, w, v):  # version 0: all in function, not preferred.
    print('iwv', i, w, v)
    if i == n:
        return v
    wi, vi = wv[i]
    if w+wi <= W:
        return max(rec(i+1, w+wi, v+vi), rec(i+1, w, v))
    else:
        return rec(i+1, w, v)

print(rec(0, 0, 0))
