# author: mofhu@github
# longest increasing subsequence

n = 6
# a = [4, 2, 3, 1, 5]
# a = [4, 2, 3, 5, 6]
a = [4, 2, 4, 4, 6, 4]

# a[i] 0/1
# i -> used index
# j -> len(LIS)
# dp[i][j] = amax
# j > amax
# dp[i+1][j+1] = j
# dp[i+1][j] = dp[i][j]
maxa = len(a) + 1
MAX = 10
dp = [[MAX for i in range(maxa)] for j in range(maxa)]
dp[0][0] = 0

for i in range(len(a)):
    dp[i][0] = 0
    for j in range(len(a)):
        if dp[i+1][j] > dp[i][j]:
            dp[i+1][j] = dp[i][j]
        if dp[i][j] < a[i]:
            if dp[i+1][j+1] > a[i]:
                dp[i+1][j+1] = a[i]
                # print(i, j, dp[i+1][j+1])
        else:
            # dp[i+1][j] = a[i]
            pass
            # break
print(dp)

ans = 0
for j in range(len(a)):
    if dp[i+1][j] != MAX:
        ans = j

print(ans)
