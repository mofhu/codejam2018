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

    while(check_even(n) == False):
        n += 1
    # print(n0, n)
    move = n - n0

    n = n0
    while(check_even(n) == False):
        n -= 1
    # print(n0, n)
    move1 = n0 -n
    if move > move1:
        move = move1

    print("Case #{}: {}".format(case, move))

    # print(d2)

