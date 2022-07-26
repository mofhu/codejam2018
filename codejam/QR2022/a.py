# author: mofhu@github
# Punched Cards

ncase = int(input())

for case in range(1, ncase+1):
    r, c = input().split(' ')
    r, c = int(r), int(c)
    print("Case #{}:".format(case))
    ans = []
    for i in range(r):
        line0 = '+-' * c + '+'
        line1 = '|.' * c + '|'
        ans.append(line0)
        ans.append(line1)
    ans.append(line0)
    ans[0] = '..' + ans[0][2:]
    ans[1] = '..' + ans[1][2:]
    for line in ans:
        print(line)
