# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by ZD Liu and Eric Martin for COMP9021


import sys
import os
import csv
import gzip

def process_file(file):
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

def str_to_num(str):
    try:
        num = int(str)
    except Exception as e:
        num = round(float(str),1)
        print(e)
    print(num)
    return num

def get_max(dic):
    max_value = 0  #!!!!!!!!!error!!!!!!!!!!!
    for country in dic.keys():
        if max(dic[country]) == '':
            continue
        tem_max = str_to_num(max(dic[country]))
        if tem_max >= max_value:
            max_value = tem_max
    return max_value

def get_max_value_year(dic, max_value):
    max_value_year = {}
    for country in dic.keys():
        for i in range(len(dic[country])):
            if dic[country][i] == '':
                pass
            elif str_to_num(dic[country][i]) == max_value:
                if first_year+i in max_value_year.keys():
                    max_value_year[first_year+i].append(country)
                else:
                    max_value_year[first_year+i] = [country]
    return  max_value_year



filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    res_dic = process_file(file)
    max_value = get_max(res_dic)
    countries_for_max_value_per_year = get_max_value_year(res_dic, max_value)


if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                    for year in sorted(countries_for_max_value_per_year)
                    )
          )


