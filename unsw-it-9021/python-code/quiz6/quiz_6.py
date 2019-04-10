#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-6 10:23
# @Author  : ZD Liu
# from random import seed, randint
# import sys
#
#
# def display_grid():
#     for i in range(len(grid)):
#         print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
#
# def size_of_largest_isosceles_triangle(): # don't copy
#     count_list = []
#     for i in range(0,10):
#         for j in range(0,10):
#             if grid[i][j] == 0:
#                 count_list.append(0)
#             else:
#                 count_down = find_triangle_d(j, j + 1, i)
#                 count_up = find_triangle_u(j, j + 1, i)
#                 count_left = find_triangle_l(j, i + 1, i)
#                 count_right = find_triangle_r(j, i + 1, i)
#                 count_list.append(max(count_down,count_up,count_left,count_right))
#     return max(count_list)
#
# def find_triangle_d(y_least,y_most,x):# don't copy
#     count =1
#     lis = [[x,i]for i in range(y_least,y_most)]
#     if justy_d(lis):
#         count = find_triangle_d(y_least-1,y_most+1, x+1)
#         count += 1
#     else:
#         count = count
#     return count
#
# don't copy
# def justy_d(lis):
#     # tt = True
#     for lis1 in lis:
#         x = lis1[0]
#         y = lis1[1]
#         try:
#             if grid[x+1][y] and grid[x+1][y-1] and grid[x+1][y+1] and y-1>=0 and y+1 <10 and x + 1 < 10:
#                 # tt = True
#                 pass
#             else:
#                 return False
#         except:
#             return False
#     return True
#
# def find_triangle_u(y_least,y_most,x):
#     count =1
#     lis = [[x,i]for i in range(y_least,y_most)]
#     if justy_u(lis):
#         count = find_triangle_u(y_least-1,y_most+1, x-1)
#         count += 1
#     else:
#         count = count
#     return count
# 
# def justy_u(lis):
#     for lis1 in lis:
#         x = lis1[0]
#         y = lis1[1]
#         try:
#             if grid[x-1][y] and grid[x-1][y-1] and grid[x-1][y+1] and y-1>=0 and y+1 <10 and x - 1 >= 0:
#                 # tt = True
#                 pass
#             else:
#                 return False
#         except:
#             return False
#     return True
#
# don't copy
# def find_triangle_l(y,x_most,x_least):
#     count =1
#     lis = [[i,y]for i in range(x_least,x_most)]
#     if justy_l(lis):
#         count = find_triangle_l(y+1 ,x_most+1, x_least-1)
#         count += 1
#     else:
#         count = count
#     return count
#
# def justy_l(lis):
#     for lis1 in lis:
#         x = lis1[0]
#         y = lis1[1]
#         try:
#             if grid[x][y+1] and grid[x+1][y+1] and grid[x-1][y+1] and x-1>=0 and y+1 <10 and x + 1 < 10:
#                 pass
#             else:
#                 return False
#         except:
#             return False
#     return True
#
# def find_triangle_r(y,x_most,x_least):
#     count =1
#     lis = [[i,y]for i in range(x_least,x_most)]
#     if justy_r(lis):
#         count = find_triangle_r(y-1 ,x_most+1, x_least-1)
#         count += 1
#     else:
#         count = count
#     return count
#
# def justy_r(lis):
#     for lis1 in lis:
#         x = lis1[0]
#         y = lis1[1]
#         try:
#             if grid[x][y-1] and grid[x+1][y-1] and grid[x-1][y-1] and x-1>=0 and y-1>=0 and x + 1 < 10:
#                 pass
#             else:
#                 return False
#         except:
#             return False
#     return True
#
# try:
#     arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()
# seed(arg_for_seed)
# grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
# print('Here is the grid that has been generated:')
# display_grid()
# print('The largest isosceles triangle has a size of',
#       size_of_largest_isosceles_triangle()
#      )
#
#
# # for arg_for_seed in range(14,16):
# #     for density in [14,15,16,17]:
# #         print(">>> print(os.popen('echo "+str(arg_for_seed)+" "+str(density)+" | python3 quiz_6.py').read(), end='')")
# #         seed(arg_for_seed)
# #         grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
# #         print('Enter two integers: Here is the grid that has been generated:')
# #         display_grid()
# #         print('The largest isosceles triangle has a size of',
# #               size_of_largest_isosceles_triangle()
# #              )
