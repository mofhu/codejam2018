# author: mofhu@github
# C - Min Max Pair

n = int(input())
a = [int(s) for s in input().split(' ')]

ans = 0
nii = 0
nij = 0
for i in range(n):
    if a[i] == i+1:
        nii += 1
    elif a[a[i]-1] == i+1:
        nij += 1

ans = nij // 2 + nii * (nii-1) // 2
print(ans)
