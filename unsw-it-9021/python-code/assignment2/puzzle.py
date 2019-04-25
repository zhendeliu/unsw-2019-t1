#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 21:37
# @Author  : ZD Liu









def puzzle_func(xml1,xml2):

    return True





if __name__ == '__main__':
    path1 = 'pieces_A.xml'
    path2 = 'pieces_AA.xml'
    with open(path1) as ff:
        xml = ff.read()
    with open(path2) as ff:
        xml2 = ff.read()
    res = puzzle_func(xml,xml2)
    print('result is ', res)