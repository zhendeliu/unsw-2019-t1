#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-10 16:38
# @Author  : ZD Liu

'''
1.旋转组合
    1.1 计算要结果图形的边长
    1.2 遍历碎片 组合出边长能相等的
    1.3 根据以相等边长图形组为基准 继续找其他边长相等的图形组
    1.4 判断是否能够拼接 #老师说明了边可以重复 仍然是
    1.5 记录能拼接的所有可能的边的坐标
2.对比得到solution
    2.1 遍历所有可能的拼接
    2.2 组合结果使用方法2对比图形是否相同
'''
def get_corrd(coordinate):
    lis_location = coordinate.strip().split(' ')
    lis_location = [i for i in lis_location if i != ''  ] # and ' ' not in i
    i = 0
    coordinate_pair = {}
    for lo in range(len(lis_location)):
        #print(lis_location)
        if 'L' in lis_location[lo].upper() or 'M' in lis_location[lo].upper():
            coordinate_pair[i] = [int(lis_location[lo+1]),int(lis_location[lo+2])]
            i += 1
        elif 'Z' in lis_location[lo].upper():
            coordinate_pair[i] = [int(lis_location[1]),int(lis_location[2])]
    return coordinate_pair


def judge_each_path(text):
    soup = BeautifulSoup(text, 'xml')
    all_path = soup.find_all('path')
    res_lis = []
    for i in range(len(all_path)):
        str_loc = all_path[i].get('d')
        corr_dic = get_corrd(str_loc)
        res_lis.append(corr_dic)
    return res_lis

def edges_length(coor_pairs):
    lens_lis = []
    for i in range(len(coor_pairs)-1):
        lens = sqrt((coor_pairs[i][0] - coor_pairs[i+1][0]) ** 2 + (coor_pairs[i][1] - coor_pairs[i+1][1])**2)
        lens_lis.append(lens)
    return lens_lis

def read_xml(file_path):
    with open(file_path) as ff:
        xml_content = ff.read()
    return xml_content

# main function for third question
def is_solution():
    path1 = ''
    path2 = '' #结果图
    pattern1 = read_xml(path1)
    pattern2 = read_xml(path2)

    return
