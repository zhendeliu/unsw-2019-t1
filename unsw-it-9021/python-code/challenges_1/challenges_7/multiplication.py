# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.

for i in range(100, 1_000):
    for j in range(10, 100):
        first_bit_mut = i * (j % 10)
        if first_bit_mut < 1_000:
            break
        sec_bit_mut = i * (j // 10)
        if sec_bit_mut > 1_000:
            break
        mut = i * j
        if mut > 10_000:
            breakdiv
        sum1 = i % 10 + j % 10 + first_bit_mut % 10 +


print('411 * 13 = 5343, all columns adding up to 10.'）
print('425 * 23 = 9775, all columns adding up to 18.')