# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

# Insert your code here


num = input('Input a nonnegative integer:')
try:
    num = int(num)
    if num < 0:
        print('Incorrect input, giving up.')
    else:
        fac = factorial(num)
        # first method
        i = 0
        fac_int = fac
        while fac_int % 10 == 0:
            fac_int = fac_int // 10
            i += 1
        print('Computing the number of trailing 0s in '+str(num)+'! by dividing by 10 for long enough: '+ str(i))
        # second method
        fac_str = str(fac)
        n = -1
        while fac_str[n] == '0':
            n -= 1
        n_str = str(-1 * (n+1))
        print('Computing the number of trailing 0s in '+str(num)+'! by converting it into a string: '+ str(i))
        # third method
        div_5 = 0
        div_2 = 0
        for m in range(num):
            m += 1
            if m % 5 == 0:
                div_5 += 1
                q = 2
                while 5 ** q <= num:
                    if m % (5**q) == 0:
                        div_5 += 1
                    q += 1
            elif m % 2 == 0:
                div_2 += 1
        count = min(div_2,div_5)
        print('Computing the number of trailing 0s in '+str(num)+'! the smart way: '+str(count))

except:
    print('Incorrect input, giving up.')
