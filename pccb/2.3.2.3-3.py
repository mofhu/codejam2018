# author: mofhu@github

n = 3
a = [3, 5, 8]
m = [3, 2, 2]
k = 100

# v2 whole sum (m is used)
am = len(a) + 10
km = k + am + 10

dp = [[-1 for i in range(km)] for j in range(am)]

for i in range(len(a)):
    dp[i][0] = 1
    for j in range(k):
        # key: remove triple cycle and only cycle with k
        if dp[i][j] >= 0:
            dp[i+1][j] = m[i]
        elif j < a[i] or dp[i+1][j-a[i]] <= 0:
            dp[i+1][j] = -1
        else:
            dp[i+1][j] = dp[i+1][j-a[i]] - 1
            # print(i+1, j-a[i])
    #print(dp[i+1])

print(dp[len(a)][:k+1])
for i in range(k):
    # print(i)
    if dp[len(a)][i] >= 0:
        print(i)
        '''
if dp[len(a)][k] == 0:
    print('No')
else:
    print('Yes')
    '''



