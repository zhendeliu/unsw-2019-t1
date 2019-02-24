
'''
Prompts the user for a seed for the random number generator,
and for a strictly positive number, nb_of_elements.
Generates a list of nb_of_elements random integers between 0 and 99, prints out the list,
computes the difference between the largest and smallest values in the list without using
the builtins min() and max(), prints it out, and check that the result is correct using
the builtins.
'''


from random import seed, randint
import sys


# Insert your code here
print('TEST 1 BEGIN')
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
rand_list = [randint(0,99) for _ in range(nb_of_elements)]
print('\nThe list is:', rand_list)
min_value = rand_list[0]
max_value = rand_list[0]
for i in rand_list:
    if i >= max_value:
        max_value = i
    elif i <= min_value:
        min_value = i
# print('\nThe minimum number in this list is:',min_value)
print('\nThe maximum difference between largest and smallest values in this list is:',max_value - min_value)
# print('Confirming with builtin operation:', min(rand_list))
print('Confirming with builtin operation:', max(rand_list) - min_value)
print('TEST 1 END')



