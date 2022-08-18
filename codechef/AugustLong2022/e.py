# author: mofhu@github
# Hello Equation

t = int(input())
from math import sqrt, floor

def isprime(n):
    for i in range(2, floor(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True

# print(isprime(2000000000))
# print(isprime(199))

'''
def sieve(n):
    # find primes less than n
    primes = set([i for i in range(n+1)])
    is_p = [True for i in range(n+1)]
    is_p[0] = False
    is_p[1] = False
    for i in range(n):
        if is_p[i] == True:
            for j in range(2*i, n+1, i):
                is_p[j] = False
                if j in primes:
                    primes.remove(j)
    # print(primes)
    return primes

# print(sieve(200))
# primes = sieve(5000000)
'''

for ncase in range(t):
    x = int(input())
    # b=1, x = 2a+2+a = 3a+2 (a>=1)
    # b=2, x= 2a+4+2a = 4a+4 (a>=1)
    # x = (b+2)a + 2b
    # b=3, x= 5a+6
    # b=4, x= 6a+8 (2*(3a+4))
    # b=5, x= 7a+10
    # b=6, x= 8a+12 (must be 4a+4)
    # b=7, x= 9a+14 (must be 3a+2)
    # could only consider primes of (b+2)
    # make p = b+2, x = p*a + 2*p - 4
    # x+4 = p*(a+2)
    # so if x+4 is prime, output 'NO'
    # elif x+4 = 2*p (a must == 0) output 'NO'
    if x <= 1000:
        b = 1
        while 2 * b + b+2 <= x:
            if (x - 2*b) % (b+2) == 0:
                ans = 'YES'
                break
            else:
                b += 1
        else:
            ans = 'NO'
    else:
        if isprime(x+4):
            ans = 'NO'
        elif (x+4)%2 == 0 and isprime((x+4) // 2):
            ans = 'NO'
        else:
            ans = 'YES'

    print(ans)


