# author: mofhu@github
# A. Everyone Loves to Sleep

t = int(input())

for ncase in range(1, t+1):
    n, h, m = [int(s) for s in input().split(' ')]
    alarms = []
    for i in range(n):
        hi, mi = [int(s) for s in input().split(' ')]
        alarms.append((hi,mi))
    alarms.sort()
    for i in alarms:
        hi, mi = i
        if hi >= h and mi >= m or hi > h:
            if mi >= m:
                ans = f'{hi-h} {mi-m}'
            else:
                ans = f'{hi-h-1} {60+mi-m}'
            print(ans)
            break
    else:
        hi, mi = alarms[0]
        if mi >= m:
            ans = f'{24+hi-h} {mi-m}'
        else:
            ans = f'{24+hi-h-1} {60+mi-m}'
        print(ans)

