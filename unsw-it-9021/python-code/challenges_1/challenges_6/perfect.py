# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

# Insert your code here

num = input('Input an integer: ')
try:
    N = int(num)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
perfect_lis = []
for i in range(2, N + 1):
    tem_list = [1]
    for j in range(2, (i//2)+1 ):
        if i % j == 0:
            tem_list.append(j)
    # print(sum(tem_list))
    if sum(tem_list) == i:
        perfect_lis.append(i)
for x in perfect_lis:
    print(str(x) + ' is a perfect number.')
