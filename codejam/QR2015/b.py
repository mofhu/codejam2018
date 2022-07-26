def main():
    n = int(input())

    for case in range(1, n + 1):
        d = int(input())
        guys = [int(s) for s in input().split(" ")]
        # print(d, guys)
        guys = sorted(guys, reverse=True)
        # print(d, guys)
        print("Case #{}: {}".format(case, cal_move(d, guys)))


def cal_move(d, guys, moved=0):
    """special move for single 9."""
    # print(d, guys, moved)
    unmove = guys[0]
    if unmove == 9 and d == 1:
        return 5
    if unmove == 9 and d > 1 and guys[1] <= 3:
        return 5
    if unmove == 9 and d > 1 and guys[1] <= 6 and (d == 2 or (d > 2 and guys[2] <= 3)):
        # special case of 9, 6, 2, min_move = 6 (333 6 2, 333 33 2)
        # and special case of 9 6.
        move_guys = guys
        del move_guys[0]
        move_guys.append(3)
        move_guys.append(3)
        move_guys.append(3)
        move_guys = sorted(move_guys, reverse=True)
        move_n = cal_move(d+1, move_guys.copy(), moved+1)
        if move_n < unmove:
            return move_n + 2
        else:
            return unmove + 1
    elif unmove <= 2:
        return unmove
    else:
        move_guys = guys
        del move_guys[0]
        if unmove % 2 == 0:
            move_guys.append(int(unmove / 2))
            move_guys.append(int(unmove / 2))
        else:
            move_guys.append(int((unmove+1) / 2))
            move_guys.append(int((unmove-1) / 2))
            # special 9 here
        move_guys = sorted(move_guys, reverse=True)
        """
        print(move_guys)
        print(cal_move(d+1, move_guys, moved+1))
        print(move_guys)
        print("before add.")
        print(move_guys)
        print(cal_move(d+1, move_guys, moved+1))
        """
        move_n = cal_move(d+1, move_guys.copy(), moved+1)
        if move_n < unmove:
            return move_n + 1
        else:
            return unmove


def test_iter(i):
    if i == 1:
        return i
    else:
        return test_iter(i-1) * i


main()
