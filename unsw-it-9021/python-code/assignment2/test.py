#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-16 22:02
# @Author  : ZD Liu


from tangram import *

# first question
file = open('pieces_AA.xml')
coloured_pieces = available_coloured_pieces(file)
print(are_valid(coloured_pieces))


# second question
file = open('pieces_A.xml')
coloured_pieces1 = available_coloured_pieces(file)
file = open('pieces_AA.xml')
coloured_pieces2 = available_coloured_pieces(file)
print(are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces_2))


# third question
file = open('shape_A_1.xml')
shape = available_coloured_pieces(file)
file = open('tangram_A_1_a.xml')
tangram = available_colored_pieces(file)
print(is_solution(tangram,shape))
