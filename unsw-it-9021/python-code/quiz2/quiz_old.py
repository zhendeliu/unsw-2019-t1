#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-05 12:45
# @Author  : ZD Liu

# Written by ZD Liu and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}


def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for kv_tup in rule.items():
        print('After ' + str(kv_tup[0][0]) + ' followed by ' + str(kv_tup[0][1]) + ', we draw ' + str(kv_tup[1]))
    # INSERT YOUR CODE HERE TO PRINT 4 LINES


def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).


    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    # INSERT YOUR CODE HERE TO PRINT ONE LINE
    if type(rule_nb) == int and rule_nb >= 0 and rule_nb <= 15:
        rule = rule_encoded_by(rule_nb)
    else:
        # print('wrong rule_nb')
        return
    if first not in [0, 1] or second not in [0, 1]:
        return
    obj_list = [first, second]
    if length < 1:
        obj_list = []
        # print('empty')
    elif length == 1:
        obj_list = [first]
        # print(obj_list)
    else:
        for i in range(length - 2):
            obj_list.append(rule[obj_list[i], obj_list[i + 1]])
    res = ''.join([str(symbol) for symbol in obj_list])
    print(res)
    return res


def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    rul_list = {}
    for n in range(15):
        rul_list[n] = rule_encoded_by(n)

    tem_dic = {}
    for i in range(len(line) - 2):
        if (int(line[i]), int(line[i + 1])) not in tem_dic.keys():
            tem_dic[(int(line[i]), int(line[i + 1]))] = int(line[i + 2])
        elif tem_dic[(int(line[i]), int(line[i + 1]))] == int(line[i + 2]):
            pass
        else:
            return -1

    lis = range(15)
    for tem_key in tem_dic.keys():
        lis2 = []
        for n in lis:
            if rul_list[n][tem_key] == tem_dic[tem_key]:
                lis2.append(n)
        lis = lis2
    if len(lis) == 1:
        return lis[0]
    else:
        return -1

    pass
    # REPLACE pass ABOVE WITH YOUR CODE



