# author: mofhu@github
# Pass the Exam

t = int(input())
for ncase in range(t):
    a, b, c = [int(s) for s in input().split(' ')]
    if a >= 10 and b >= 10 and c >= 10:
        if a + b + c >= 100:
            print('PASS')
            continue
    print('FAIL')
