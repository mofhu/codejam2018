# author: mofhu@github
# C. Word Game

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s1 = [i for i in input().split(' ')]
    s2 = [i for i in input().split(' ')]
    s3 = [i for i in input().split(' ')]
    w1 = {}
    w2 = {}
    w3 = {}
    for w in s1:
        w1[w] = [0]
    for w in s2:
        if w in w1:
            w2[w] = [0,1]
            del w1[w]
        else:
            w1[w] = [1]
    for w in s3:
        if w in w2:
            # w3[w] = [1,2,3]
            del w2[w]
        elif w in w1:
            w2[w] = w1[w] + [2]
            del w1[w]
        else:
            w1[w] = [2]
    score = [0, 0, 0]
    for w in w1:
        score[w1[w][0]] += 3
    for w in w2:
        # print(w2[w])
        score[w2[w][0]] += 1
        score[w2[w][1]] += 1
    print('{} {} {}'.format(score[0], score[1], score[2]))

