# author: mofhu@github
# A - World Cup

y = int(input())
if y % 4 == 2:
    ans = y
elif y % 4 < 2:
    ans = (y // 4) * 4 + 2
else:
    ans = (y // 4) * 4 + 6
print(ans)
