#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-18 20:52
# @Author  : ZD Liu


import sys
import os
import csv
import gzip

def process_file(file, indicator_of_interest):
    dic_indicator = {}
    for i in file:
        try:
            if i == []:
                continue
            if i[2] == indicator_of_interest.strip():
                for m in range(len(i)):
                    dic_indicator[i[0]] = i[4:]
        except Exception as e:
            pass
    return dic_indicator


def process_maxvalue(dic):
    dic_not_none = {}
    max_value_year = {}
    for dic_key in dic.keys():
        for i in range(len(dic[dic_key])):
            if dic[dic_key][i] == '':
                pass
            else:
                dic_not_none[(dic_key,i+first_year)] = float(dic[dic_key][i])
    max_value = max(dic_not_none.values())
    for key in dic_not_none.keys():
        if dic_not_none[key] == max_value:
            if  key[1] in max_value_year.keys():
                max_value_year[key[1]].append(key[0])
            else:
                max_value_year[key[1]] = [key[0]]
    return max_value, max_value_year


def main2(indicator_of_interest):
    filename = 'HNP_Data.csv.gz'
    if not os.path.exists(filename):
        print(f'There is no file named {filename} in the working directory, giving up...')
        sys.exit()

    with gzip.open(filename) as csvfile:
        file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
        res_dic = process_file(file,indicator_of_interest)
        if len(res_dic.keys()) > 0:
            max_value , countries_for_max_value_per_year = process_maxvalue(res_dic)
            if max_value != None :
                if max_value % 1 ==0:
                    max_value = int(max_value)


    if max_value is None:
        print('Sorry, either the indicator of interest does not exist or it has no data.')
    else:
        print('The maximum value is:', max_value)
        print('It was reached in these years, for these countries or categories:')
        print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                        for year in sorted(countries_for_max_value_per_year)
                        )
              )





# indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}
# main2(indicator_of_interest)
