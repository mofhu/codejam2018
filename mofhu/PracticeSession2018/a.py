ncase = int(input())

for case in range(1, ncase+1):
    a, b = [int(s) for s in input().split(" ")]
    a += 1
    n = int(input())
    guess = int(round((a+b)/2, 0))
    print(guess)
    ans = input()

    while ans != "CORRECT":
        if ans == "TOO_BIG":
            if b == guess:
                b -= 1
            else:
                b = guess
        else:
            if a == guess:
                a += 1
            else:
                a = guess
        guess = int(round((a+b)/2, 0))
        print(guess)
        ans = input()
    # print(d2)

