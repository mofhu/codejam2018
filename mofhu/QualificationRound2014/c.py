ncase = int(input())

for case in range(1, ncase + 1):
    r, c, m = [int(i) for i in input().split(" ")]
    # print(r, c, m)
    """
    strategy: let every empty cell connect to 0 cell. (or only 1 cell without mine)
    small case version: enumerate and proof.
    """
