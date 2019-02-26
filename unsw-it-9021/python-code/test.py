#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-25 19:09
# @Author  : ZD Liu

'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''

from random import seed, randrange
import sys

# Prompts the user for a seed for the random number generator,
# and for a strictly positive number, nb_of_elements.
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
# Generates a list of nb_of_elements random integers between 0 and 99.
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:', L)
print()

less = [0] * 4
for e in L:
    if e < 5:
        less[0] += 1
    elif e > 4 and e < 10:
        less[1] += 1
    elif e > 9 and e < 15:
        less[2] += 1
    elif e > 14 and e < 20:
        less[3] += 1

if less[0] == 0:
    print('There is no element between 0 and 4.')
elif less[0] == 1:
    print('There is', less[0], 'element', 'between 0 and 4.')
elif less[0] > 1:
    print('There are', less[0], 'elements', 'between 0 and 4.')
if less[1] == 0:
    print('There is no element between 5 and 9.')
elif less[1] == 1:
    print('There is', less[1], 'element', 'between 5 and 9.')
elif less[1] > 1:
    print('There are', less[0], 'elements', 'between 5 and 9.')

if less[2] == 0:
    print('There is no element between 10 and 14.')
elif less[2] == 1:
    print('There is', less[2], 'element', 'between 10 and 14.')
elif less[2] > 1:
    print('There are', less[2], 'elements', 'between 10 and 14.')

if less[3] == 0:
    print('There is no element between 15 and 19.')
elif less[3] == 1:
    print('There is', less[3], 'element', 'between 15 and 19.')
elif less[3] > 1:
    print('There are', less[3], 'elements', 'between 15 and 19.')












