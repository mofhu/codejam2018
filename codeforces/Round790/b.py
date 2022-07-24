# author: mofhu@github
# B. Equal Candies

ncase = int(input())

for case in range(1, ncase+1):
    n = int(input())
    s = [int(i) for i in input().split(' ')]
    ans = sum(s) - n*min(s)
    print("{}".format(ans))


