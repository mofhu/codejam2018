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

# input
n = int(input())
k = int(input())
t = int(input())
r = int(input())
sinr = []
for i in range(r*k*t):
    line = [float(s) for s in input().split(' ')]
    sinr.append(line)
d = []
for i in range(n*r*k):
    line = [float(s) for s in input().split(' ')]
    d.append(line)
j = int(input())
frames = []
for i in range(j):
    line = [int(s) for s in input().split(' ')]
    frames.append(line)

print(sinr)
print(d)
print(frames)
