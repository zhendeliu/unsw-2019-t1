#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-03 22:57
# @Author  : ZD Liu

from quiz_2 import *
def quiz2_test():
    describe_rule(3)
    describe_rule(4)
    describe_rule(11)
    describe_rule(14)
    describe_rule('')
    describe_rule(0)
    describe_rule('a')
    print(draw_line(3, 0, 0, 1))
    print(draw_line(3, 0, 0, 1))
    print(draw_line(3, 0, 0, 1))
    print(draw_line(3, 1, 0, 5))
    print(draw_line(4, 1, 0, 9))
    print(draw_line(4, 0, 1, 13))

    print(draw_line(11,1,0,16))
    print(draw_line(11, 1, 1, 19))
    print(draw_line(14, 0, 0,21))
    print(draw_line(15, 0,0,22))
    print(draw_line(4, 0, 1, 13))
    print(999)
    print(draw_line(-4, 0, 1, 13))
    print(draw_line(4, -1, 1, 13))
    print(draw_line(4, 0, -1, 13))
    print(draw_line(4, 2, 1, 13))
    print(draw_line(4, 0, 2, 13))
    print(draw_line(0,0,0,0))
    print(draw_line(1,1,1,1))
    print(draw_line(4, 0, 1, 0))
    print(draw_line('a', 0, 1, 0))
    print(draw_line(4, 'a', 1, -1))
    print(draw_line(4, 0, 'a', 13))
    print(draw_line(4, 0, 1, 'a'))
    print(draw_line(4, 0, 1, ''))
    print(draw_line(4, 0, '', 13))
    print(draw_line(4, '', 1, 13))
    print(draw_line('', 0, 1, 13))
    print(draw_line(1, 1, 1, 8))
    print(draw_line(3, 1, 1, 8))
    print(uniquely_produced_by_rule('1100110011'))
    print(uniquely_produced_by_rule('01100000'))
    print(uniquely_produced_by_rule('001101101'))
    print(uniquely_produced_by_rule('11111111'))
    print(uniquely_produced_by_rule('00011'))
    print(uniquely_produced_by_rule('11001'))
    print(uniquely_produced_by_rule('0010001'))
    print(uniquely_produced_by_rule('0010001'))
    print(uniquely_produced_by_rule('1111111111111111111111111'))
    print(uniquely_produced_by_rule(111))
    print(uniquely_produced_by_rule(101))
    print(uniquely_produced_by_rule('0'))
    print(uniquely_produced_by_rule('00'))
    print(uniquely_produced_by_rule('01'))
    print(uniquely_produced_by_rule('11'))
    print(uniquely_produced_by_rule('[]'))
    print(uniquely_produced_by_rule('ccc'))




if __name__ == '__main__':
    quiz2_test()
    a = []
    if i not in