'''
Prints out a conversion table of temperatures from Celsius to Fahrenheit degrees,
the former ranging from 0 to 100 in steps of 10.
'''


# Insert your code here
# -*- coding: utf-8 -*-
# @Time    : 2019-02-23 16:10
# @Author  : ZD Liu
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
