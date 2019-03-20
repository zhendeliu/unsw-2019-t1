#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-20 19:25
# @Author  : ZD Liu


import sys
from random import seed, randint, randrange
import quiz_4_2 as q4



if __name__ == '__main__':
    import doctest
    print('test start.....')
    with open('indicator.txt') as f:
        line_list = f.readlines()
        for line in line_list:
            print('>>> ' + line)
            q4.main2(line)


    #doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass all my test')