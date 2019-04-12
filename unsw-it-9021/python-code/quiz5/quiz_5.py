# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by ZD Liu and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def encode_list(encoded_set):
    bin_str = bin(encoded_set)[2:]
    str_lenth = len(bin_str)
    res_lis = []
    for i in range(str_lenth):
        if i % 2 == 0 and bin_str[-(i + 1)] == '1':
            c = i // 2
            res_lis.append(c)
        elif bin_str[-(i + 1)] == '1':
            c = -i // 2
            res_lis.append(c)
    res_lis.sort()
    for i in range(len(res_lis)):
        res_lis[i] = str(res_lis[i])
    return res_lis

# POSSIBLY DEFINE OTHER FUNCTIONS    
def display_encoded_set(encoded_set):
    res_lis = encode_list(encoded_set)
    print('{',end='')
    print(', '.join(res_lis), end='}\n')
    pass
    # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)


def code_derived_set(encoded_set):
    encoded_running_sum = 0
    # REPLACE THIS COMMENT WITH YOUR CODE
    lis = encode_list(encoded_set)
    tem_sum = 0
    tem_lis = []
    for i in range(len(lis)):
        tem_sum += int(lis[i])
        if tem_sum not in tem_lis:
            tem_lis.append(tem_sum)
        else:
            continue
        if tem_sum < 0:
            encoded_running_sum += 2 ** (- tem_sum * 2 - 1)
        else:
            encoded_running_sum += 2 ** (tem_sum * 2 )
    return encoded_running_sum

print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)

