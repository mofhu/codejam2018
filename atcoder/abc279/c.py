# author: mofhu@github
# C - RANDOM

h, w = [int(s) for s in input().split(' ')]
from collections import Counter  # set can not work: duplicates, use Counter (multiset) instead.

s_row = []

for i in range(h):
    s_row.append(input())

s_col = []
for i in range(w):
    s_col.append(''.join([s_row[j][i] for j in range(h)]))
# print(s_col)
s = Counter(s_col)

t_row = []
for i in range(h):
    t_row.append(input())

t_col = []
for i in range(w):
    t_col.append(''.join([t_row[j][i] for j in range(h)]))

t = Counter(t_col)

if s == t:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
