ncase = int(input())


for case in range(1, ncase+1):
    # print(case)
    a, b = [int(s) for s in input().split(" ")]
    n = int(input())

    while (True):
        guess = int(round((a+b+0.1) / 2, 0))
        if guess == a:
            guess += 1
        print(guess)
        s = input()
        if s == "CORRECT":
            break
        elif s == "TOO_SMALL":
            a = guess
        else:
            b = guess


