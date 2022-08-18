# author: mofhu@github

n = 3
a = [3, 5, 8]
m = [3, 2, 2]
k = 17

# v1 ignore m, simpler sum
am = len(a) + 10
km = k + am + 10

dp = [[0 for i in range(km)] for j in range(am)]

for i in range(len(a)):
    dp[i][0] = 1
    for j in range(k):
        if dp[i][j] != 0:
            dp[i+1][j] = 1
            dp[i+1][j+a[i]] = 1

print(dp[len(a)][:k+1])
if dp[len(a)][k] == 0:
    print('No')
else:
    print('Yes')


