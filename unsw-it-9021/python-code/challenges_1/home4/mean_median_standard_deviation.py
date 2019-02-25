# Written by Eric Martin for COMP9021


'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between -50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways,
that is, using or not the functions from the statistics module, and prints them out.
'''


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys


# Insert your code here
def find_median(obj_list):
    # ord_list = obj_list[0]
    # for i in range(len(obj_list)):
    #     for j in range(len(obj_list)-i):
    #         if obj_list[i]

    for i in range(0, len(obj_list)):
        min = i
        for j in range(i + 1, len(obj_list)):
            if obj_list[min] > obj_list[j]:
                min = j
        obj_list[min], obj_list[i] = obj_list[i], obj_list[min]
    if len(obj_list) % 2 == 0:
        res = (obj_list[int(len(obj_list)/2)] + obj_list[int(len(obj_list)/2 - 1)]) / 2
    else:
        res = obj_list[int(len(obj_list)/2)]
    return res
def compute_mean(obj_list):
    sum = 0
    for i in obj_list:
        sum += i
    res = float(sum)/len(obj_list)
    return res
def standard_deviation(obj_list, obj_mean):
    sum_pow = 0
    for i in obj_list:
        sum_pow += (i - obj_mean) ** 2
    res = sqrt(sum_pow / len(obj_list))
    return res
try:
    seed_value = int(input('Input a seed for the random number generator:'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate?'))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
seed(seed_value)
rand_list = [randint(-50,50) for _ in range(nb_of_elements)]
print('\nThis list is:',rand_list)

print()
print('The mean is ' + format(compute_mean(rand_list),'0.2f')+ '.')
print('The median is '+ format(find_median(rand_list),'0.2f') +'.')
print('The standard deviation is ' + format(standard_deviation(rand_list, compute_mean(rand_list)),'0.2f') +'.')
print('\nConfirming with functions from the statistics module:')
print('The mean is ' + format(mean(rand_list),'0.2f') + '.')
print('The median is '+ format(median(rand_list),'0.2f') +'.')
print('The standard deviation is ' + format(pstdev(rand_list),'0.2f') +'.')
