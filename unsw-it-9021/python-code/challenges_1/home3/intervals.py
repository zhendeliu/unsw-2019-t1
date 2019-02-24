'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''


from random import seed, randrange
import sys


# Insert your code here
def solution1():
    try:
        seed_value = int(input('Input a seed for the random number generator: '))
    except ValueError:
        print('Input is not an integer, giving up.')
        sys.exit()
    try:
        nb_of_elements = int(input('How many elements do you want to generate? '))
        if nb_of_elements <= 0:
            print('Input should be strictly positive, giving up.')
            sys.exit()
    except ValueError:
        print('Input is not an integer, giving up.')
        sys.exit()
    seed(seed_value)
    rand_list = [randrange(19) for _ in range(nb_of_elements)]
    print('\nThe list is:', rand_list)
    print()
    count_dic = {}
    count_dic[(0, 4)] = 0
    count_dic[(5, 9)] = 0
    count_dic[(10, 14)] = 0
    count_dic[(15, 19)] = 0
    for i in rand_list:
        if i >= 0  and i <= 4 :
            count_dic[(0, 4)] += 1
        if i >= 5 and i <= 9:
            count_dic[(5, 9)] += 1
        if i >= 10 and i <= 14:
            count_dic[(10, 14)] += 1
        if i >= 15 and i <= 20:
            count_dic[(15, 19)] += 1
    for counts in count_dic.items():
        if count_dic[counts[0][0],counts[0][1]] == 0:
            print('There is no element between '+str(counts[0][0])+' and '+str(counts[0][1])+'.')
        elif count_dic[counts[0][0],counts[0][1]] == 1:
            print('There is 1 element between '+str(counts[0][0])+' and '+str(counts[0][1])+'.')
        else:
            print('There are '+str(count_dic[counts[0][0],counts[0][1]])+' elements between '+str(counts[0][0])+' and '+str(counts[0][1])+'.')

# ==============solution 2 ================================
try:
    seed_value = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
    if nb_of_elements <= 0:
        print('Input should be strictly positive, giving up.')
        sys.exit()
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
seed(seed_value)
rand_list = [randrange(19) for _ in range(nb_of_elements)]
print('\nThe list is:', rand_list)
print()
count_list = [0 for i in range(4)]
for num in rand_list:
    count_list[num // 5] += 1
for i in range(4):
    if count_list[i] == 0:
        print('There is no element between ' + str(i * 5) + ' and ' + str(i * 5 + 4) + '.')
    elif count_list[i] == 1:
        print('There is 1 element between ' + str(i * 5) + ' and ' + str(i * 5 + 4) + '.')
    else:
        print('There are ' + str(count_list[i]) + ' elements between ' + str(
            i * 5) + ' and ' + str(i * 5 + 4) + '.')


