# author: mofhu@github
# C. Traffic Light

t = int(input())

for ncase in range(1, t+1):
    n, c = [s for s in input().split(' ')]
    n = int(n)
    s = input()
    ans = 0
    if c == 'g':
        pass
    else:
        state = 0
        g0 = -1
        for i in range(n):
            if s[i] == c:
                if state == 0:
                    state += 1
                elif state > 0:
                    state += 1
            elif s[i] == 'g':
                if g0 == -1:
                    g0 = i
                if state == 0:
                    pass
                else:
                    if ans < state:
                        ans = state
                        # print('ans update', ans, i)
                    state = 0
            else:
                if state > 0:
                    state += 1
        else:
            if state > 0:
                state += g0
                if ans < state:
                    ans = state
                    # print('ans update', ans, i)
                    state = 0
    print(ans)


