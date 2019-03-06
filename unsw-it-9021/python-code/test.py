def display_ECA(rule_nb, size):
    bit_below = record_rule(rule_nb) # 规则创建
    new_line = [1]
    end_bit = 0
    display_line(new_line, end_bit, size) # 展示初始第一行
    for n in range(size):
        current_line = [end_bit] * 2 + new_line + [end_bit] * 2
        new_line = [bit_below[current_line[i],current_line[i + 1],current_line[i + 2]]for i in range(len(current_line) - 2)]
        end_bit = bit_below[end_bit, end_bit, end_bit]
        display_line(new_line, end_bit, size - n - 1)


def display_end_squares(end_bit, nb_of_end_bits):
    print(end_bit * nb_of_end_bits, end = '')

def display_line(bit_sequence, end_bit, nb_of_end_bits):
    squares = {0: '\u2b1c', 1: '\u2b1b'} # 定义字典 0 表示 白色方块 1 表示黑色方块
    display_end_squares(squares[end_bit], nb_of_end_bits) # 画出前一部分的白框
    print(''.join(squares[b] for b in bit_sequence), end = '')# 画出中间部分的计算得到的白框和黑框
    display_end_squares(squares[end_bit], nb_of_end_bits) # 画出后半部分的白框
    print()

def record_rule(E):
    values = [int(d) for d in f'{E:08b}'] # 列表元素对应二进制数E的所有位置的值，从前往后8位 空格用0补
    return {(p // 4, p // 2 % 2, p % 2): values[7 - p] for p in range(8)} # 创建返回规则字典，字典key来自于二进制列表


if __name__ == '__main__':
    # display_ECA(90,7)
    dic = {(1,2):1, (2,3):2}
    for i in dic.items():
        print(type(i[0]))