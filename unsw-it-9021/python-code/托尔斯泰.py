#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 18:21
# @Author  : ZD Liu


def nicely_display(sequence, max_size):
    field_width = max_size + 2
    nb_of_fields = 80 // field_width
    count = 0
    for e in sequence:
        print(f'{e:{field_width}}', end = '')
        count += 1
        if count % nb_of_fields == 0:
            print()


nicely_display(range(200), 3)