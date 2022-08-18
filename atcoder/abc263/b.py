# author: mofhu@github
# B - Ancestor

n = int(input())
p = [int(s) for s in input().split(' ')]
ans = 0
i = n-2
while(p[i] != 1):
    i = p[i] - 2
    ans += 1
ans += 1

print(ans)
