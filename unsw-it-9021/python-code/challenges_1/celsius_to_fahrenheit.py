#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-23 16:10
# @Author  : ZD Liu

def celsius_to_fahrenheit():
    import os
    print('TEST 1 BEGIN')
    print('$ python3 '+ os.path.basename(__file__))
    min_temperature = 0
    max_temperature = 100
    step = 10
    print('Celsius\tFahrenheit')
    for celsius in range(min_temperature, max_temperature + step, step):
        fahrenheit = int(celsius / step * 18 + 32)
        print(f'{celsius:7}\t{fahrenheit:10}')
    print('TEST 1 END')


if __name__ == '__main__':
    celsius_to_fahrenheit()