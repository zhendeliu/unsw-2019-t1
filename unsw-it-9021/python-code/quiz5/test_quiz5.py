#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-01 21:07
# @Author  : ZD Liu

# Written by ZD Liu and Eric Martin for COMP9021


from itertools import accumulate
import sys


def encode_list(encoded_set):
    i = 0
    res_lis = []
    while encoded_set:
        if encoded_set & 1 and i % 2 == 0:
            res_lis.append(i // 2)
        elif encoded_set & 1 and i % 2 == 1:
            res_lis.append(-i // 2)
        encoded_set = encoded_set >> 1
        i += 1
    res_lis.sort()
    return res_lis


def display_encoded_set(encoded_set):
    res_lis = encode_list(encoded_set)
    res_lis = map(lambda x: str(x), res_lis)
    print('{', end='')
    print(', '.join(res_lis), end='}\n')


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    lis = encode_list(encoded_set)
    sum_lis = set(accumulate(lis))
    for i in sum_lis:
        if i < 0:
            encoded_running_sum = encoded_running_sum + 2 ** (- i * 2 - 1)
        else:
            encoded_running_sum = encoded_running_sum + 2 ** (i * 2)
    return encoded_running_sum


try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
print('The encoded set is: ', end='')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end='')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
