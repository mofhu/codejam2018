# author: mofhu@github
# A. Game with Integers

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    if n % 3 == 0:
        ans = 'Second'
    else:
        ans = 'First'
    print(ans)




