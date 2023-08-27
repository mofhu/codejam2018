# author: mofhu@github
# B - MissingNo.

n = int(input())
a = [int(i) for i in input().split(' ')]
a.sort()

for i in range(1, n):
    if a[i] - a[i-1] != 1:
        ans = a[i] - 1
        break

print(ans)


