# author: mofhu@github
# D - Count Subtractions

a, b = [int(s) for s in input().split(' ')]

ans = 0
while a != b and a != 0 and b != 0:
    if a > b:
        ans += a // b
        a = a % b
    else:
        ans += b // a
        b = b % a

if a == b:
    print(ans)
else:
    print(ans-1)
