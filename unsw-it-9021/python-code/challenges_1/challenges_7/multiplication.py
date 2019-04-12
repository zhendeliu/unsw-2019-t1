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
            continue
        sec_bit_mut = i * (j // 10)
        if sec_bit_mut > 1_000:
            continue
        mut = i * j
        if mut > 10_000:
            continue
        sum1 = i % 10 + j % 10 + first_bit_mut % 10 + mut % 10
        sum2 = (i // 10) % 10  + j // 10 + (first_bit_mut // 10) % 10 + sec_bit_mut % 10 + (mut // 10 ) % 10
        sum3 = (i // 100)   + (first_bit_mut // 100) % 10 + (sec_bit_mut // 10) % 10 + (mut // 100 ) % 10
        sum4 = (first_bit_mut // 1000) + (sec_bit_mut // 100)  + (mut // 1000 )
        if sum1 == sum2 and sum2 ==sum3 and sum3 == sum4:
            print('%d * %d = %d, all columns adding up to %d.' % (i, j, mut, sum4))