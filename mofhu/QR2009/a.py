# GCJ Qualification Round 2009 - A
# Author: Mo Frank Hu
# best solution may be generate a dict tree and search it.

from collections import deque

l, d, n = [int(z) for z in input().split(" ")]
# print(l,d,n)

s = {}
for i in range(d):
    key = input()
    for k in range(1, len(key)+1):
        s[key[:k]] = i

# print(l,d,n)  #
# print(s)  #

for ncase in range(1, n+1):  # for each test case
    # read input
    a = [k for k in input()]
    b = []
    flag = False
    for word in a:
        if word is "(":
            flag = True
            temp = []
        elif word is ")":
            flag = False
            b.append(temp)
        elif flag is True:
            temp.append(word)
        else:
            # print(word)
            b.append(word)
    # generate possible words and test them
    words = deque()
    if len(b) > 0:
        for letter in b[0]:
            if letter in s:
                words.append(letter)
    for i in range(1, len(b)):
        char = b[i]
        if len(words) is not 0:
            l0 = len(words)
            for i in range(l0):
                t = words.popleft()
                for letter in char:
                    if t + letter in s:
                        words.append(t + letter)
    # print(words)
    # match words
    match = 0
    while len(words) > 0:
        t = words.pop()
        if t in s:
            match += 1
    print("Case #{}: {}".format(ncase, match))