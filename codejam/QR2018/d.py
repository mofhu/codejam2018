ncase = int(input())

from decimal import *
import math

for case in range(1, ncase+1):
    getcontext().prec = 58
    a = Decimal(float(input()))

    # only rotate xy with alpha to solve Ds case
    # area = (cos alpha) + (sin alpha)
    # area = (cos alpha) + sqrt(1 - cos^2 alpha)
    # (a - cos alpha)^2 = 1 - 1 cos^2 alpha
    # a^2 -2*a* cos alpha + cos^2 alpha = 1 - 1 cos^2 alpha
    # 2* cos^2 alpha - 2*a cos alpha + a^2 - 1 = 0
    # cos alpha = 1/4 *(-2*a +- sqrt[4*a^2-4*2*(a^2 - 1)])
    # print(4-8*(a*a-1))
    alpha = Decimal((-2*a + Decimal(math.sqrt(4*a*a-8*(a*a-1))) )/ 4)
    # print(alpha)
    # print(type(alpha))
    x1, y1, z1 = alpha / 2, math.sqrt((1-alpha*alpha))/2, 0
    x2, y2, z2 = math.sqrt(1-alpha*alpha)/2, 0 - alpha / 2, 0
    x3, y3, z3 = 0, 0, 0.5

    # ax2+bx+c=0
    # x2+b/ax+c/a=0
    # x2+2 *b/2ax +b2/4a2+ c/a-b2/4a2 = 0
    # (x-b/2a)2 = (b2-4ac)/4a2
    # x = (b +- sqrt(b2-4ac)) / 2a

    print("Case #{}:".format(case))
    print("{:.15f} {:.15f} {:.15f}".format(x1,y1,z1))
    print("{:.15f} {:.15f} {:.15f}".format(x2,y2,z2))
    print("{:.15f} {:.15f} {:.15f}".format(x3,y3,z3))

