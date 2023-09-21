# author: mofhu@github
# C. Target Practice

t = int(input())

for ncase in range(1, t+1):
    ans = 0
    for i in range(10):
        s = input()
        for j in range(10):
            if s[j] == 'X':
                if i == 0 or j == 0 or i == 9 or j == 9:
                    ans += 1
                elif i == 1 or j == 1 or i == 8 or j == 8:
                    ans += 2
                elif i == 2 or j == 2 or i == 7 or j == 7:
                    ans += 3
                elif i == 3 or j == 3 or i == 6 or j == 6:
                    ans += 4
                else:
                    ans += 5
    print(ans)


