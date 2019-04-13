# author: mofhu@github
# You Can Go Your Own Way

t, n, m = [int(s) for s in input().split(" ")]
import sys
x = 3*4*5*7*11*13*17

from time import sleep
sleep(0.05)
for case in range(n):

    sleep(0.05)
    hanxin = {}
    for i in (3,4,5,7,11,13,17):
        print("{}{}".format((str(i)+" ")*17, str(i)))
        sys.stdout.flush()
        sleep(0.05)
        t = input()
        reply = [int(s) for s in t.split(" ")]
        hanxin[i] = sum(reply)
    ans = 0
    # print(x, hanxin)
    for i in hanxin:
        xi0 = int(x / i)
        xi = xi0
        while(xi % i != 1):
            xi += xi0
        ans += xi*hanxin[i]
        # print("i", i, xi, ans )

    # print("i", i, xi, ans )
    ans = ans % x

    print(ans)
    sys.stdout.flush()
    sleep(0.1)
    t = input()

    sys.stdout.flush()

    sleep(0.5)
    continue


