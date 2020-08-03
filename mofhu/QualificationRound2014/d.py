ncase = int(input())

"""
War strategy:
    Naomi max to min;
    Ken if max larger than Naomi, then max; else min.
Deceitful war strategy:
    Naomi min to max;
    Ken if min smaller than Naomi, min, else max.
"""

for case in range(1, ncase+1):
    n = int(input())
    naomi = [float(i) for i in input().split(" ")]
    ken = [float(i) for i in input().split(" ")]
    naomi.sort()
    ken.sort()
    naomi0 = naomi[:]
    ken0 = ken[:]
    # print(naomi)
    # cal for deceitful war
    decietful_war_naomi = 0
    for i in range(n):
        if naomi[0] < ken[0]:
            del naomi[0]
            del ken[-1]
        else:
            decietful_war_naomi += 1
            del naomi[0]
            del ken[0]
    # cal for Ken's war strategy
    naomi = naomi0
    ken = ken0
    war_naomi = 0
    for i in range(n, 0, -1):
        if naomi[i-1] < ken[i-1]:
            del naomi[i-1]
            del ken[i-1]
        else:
            war_naomi += 1
            del naomi[i-1]
            del ken[0]
    print("Case #{}: {} {}".format(case, decietful_war_naomi, war_naomi))

    # print(c, f, x)
