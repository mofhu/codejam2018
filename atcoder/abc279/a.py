# author: mofhu@github
# A - wwwvvvvvv

s = input()

ans = 0
for i in s:
    if i == 'w':
        ans += 2
    else:
        ans += 1

print(ans)
