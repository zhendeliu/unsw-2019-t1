from math import sqrt
from collections import Counter
def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    if number <2:
        return 0
    i = 2
    lis = []
    while i < number+1 and number != 0:
        if is_prime(i):
            if number%i ==0:
                lis.append(i)
                number = number//i
#                if is_prime(number):
#                    lis.append(number)
#                    break
                
            else:
                i+=1
        else:
            i += 1
    res = set(lis)
    r = 1
    for i in res:
        r *= i
    return r
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE

def is_prime(n):
    m = int(sqrt(n)) +1
    for i in range(2,m):
        if n%i ==0:
            return 0
    return 1

#print(single_factors(154))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
