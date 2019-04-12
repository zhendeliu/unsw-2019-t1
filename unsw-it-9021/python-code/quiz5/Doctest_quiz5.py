#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 12:54
# @Author  : ZD Liu

'''
>>> encoded_set = 2
>>> print('The encoded set is: ', end = '')
>>> q5.display_encoded_set(encoded_set)
>>> encoded_running_sum = q5.code_derived_set(encoded_set)
>>> print('The derived encoded set is: ', end = '')
>>> q5.display_encoded_set(encoded_running_sum)
>>> print('  It is encoded by:', encoded_running_sum)
The encoded set is: {-1}
The derived encoded set is: {-1}
  It is encoded by: 2

'''


import quiz_5 as q5

if __name__ == '__main__':
    import doctest
    print('Test Start......')
    # doctest.testmod()
    doctest.testfile(quiz_5.py)
    print('Test Done! If not show "Test Failed", you pass my test')