# Written by ZD Liu and Eric Martin for COMP9021



import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def length_of_longest_increasing_sequence(L):
    if len(L) < 1:
        return 0
    if len(L) == 1:
        return 1
    count_list = []
    for i in range(len(L)):
        j = i+1
        if j >= len(L):
            j = 0
        count = 1
        while L[i] <= L[j]:
            count += 1
            if count >= len(L):
                return len(L)
            i += 1
            j += 1
            if i >= len(L):
                i = 0
            if j >= len(L):
                j = 0
        count_list.append(count)
    return max(count_list)
    pass
    # REPLACE pass ABOVE WITH  YOUR CODE

def max_int_jumping_in(L):
    if len(L) < 1:
        return
    num_list = []
    for i in range(len(L)):
        num_str = str(L[i])
        index_list = []
        index_list.append(i)
        index_new = L[i]
        while index_new not in index_list:
            index_list.append(index_new)
            index_new = L[index_new]
            num_str += str(index_new)
        num_list.append(int(num_str))
    return max(num_list)


seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )


