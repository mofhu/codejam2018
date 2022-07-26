ncase = int(input())


def check_even(n):
    while n > 0:
        if n % 2 != 0:
            return False
        else:
            n = int(n / 10)
            if n == 0:
                return True
    return True


for case in range(1, ncase+1):
    n = int(input())
    n0 = n

    # cal increase min
    nmin = 0
    while n>0:
        ndigit = int(str(n)[0])
        # print(n, ndigit, len(str(n)))
        if ndigit % 2 == 0:
            nmin += ndigit * (10 ** (len(str(n)) - 1))
        else:
            if ndigit != 9:
                nmin += (ndigit+1) * (10 ** (len(str(n))- 1))
            else:
                nmin += (ndigit+11) * (10 ** (len(str(n))- 1))
            break
        # print(nmin)
        n = n - ndigit * (10 ** (len(str(n)) - 1))
    # print(nmin, 'up')

    nmax = 0
    n = n0
    while n>1:
        ndigit = int(str(n)[0])
        length = len(str(n))
        # print(n, nmax, ndigit, len(str(n)))
        if ndigit % 2 == 0:
            nmax += ndigit * (10 ** (length - 1))
        else:
            if ndigit != 1:
                nmax += (ndigit-1) * (10 ** (length- 1))
            else:
                nmax += 8* (10 ** (length - 2))
                length -= 1
            while length > 1:
                nmax += 8* 10**(length-2)
                # print(8* 10**(length-2), "+")
                length -= 1
            break
        n = n - ndigit * (10 ** (length - 1))
    # print(nmax)

    if(nmin-n0 <= n0-nmax):
        move = nmin-n0
    else:
        move = n0-nmax
    print("Case #{}: {}".format(case, move))

    # print(d2)

