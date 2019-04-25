#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-09 10:03
# @Author  : ZD Liu
from math import sqrt
from bs4 import BeautifulSoup

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
    print(8888)
    print(res_lis)
    print(9999)
    return res_lis

def edges_length(coor_pairs):
    lens_lis = []
    for i in range(len(coor_pairs)-1):
        lens = sqrt((coor_pairs[i][0] - coor_pairs[i+1][0]) ** 2 + (coor_pairs[i][1] - coor_pairs[i+1][1])**2)
        lens_lis.append(lens)
    return lens_lis

def compare_list(lis1, lis2):
    for lis in [lis1, list(reversed(lis1))]:
        for i in range(len(lis)):
            tem_lis = lis[i:] + lis[:i]
            if tem_lis == lis2:
                return True

    return False


def compare_func(text1,text2):
    edge_group1 = {}
    edge_group2 = {}
    for single in judge_each_path(text1):
        if len(single) in edge_group1.keys():
            edge_group1[len(single)].append(single)
        else:
            edge_group1[len(single)] = [single]
    for single2 in judge_each_path(text2):
        if len(single2) in edge_group2.keys():
            edge_group2[len(single2)].append(single2)
        else:
            edge_group2[len(single2)] = [single2]
    if list(edge_group1.keys()).sort() == list(edge_group2.keys()).sort():
        for key in edge_group1.keys():
            if len(edge_group1[key]) == len(edge_group2[key]):
                for k in range(len(edge_group1[key])):
                    print(edge_group1[key][k])
                    e_lens1 = edges_length(edge_group1[key][k])
                    for p in range(len(edge_group2[key])):
                        print(edge_group1[key][p])
                        e_lens2 = edges_length(edge_group2[key][p])
                        if compare_list(e_lens1,e_lens2):
                            edge_group2[key].pop(p)
                            break
                if len(edge_group2[key]) != 0:
                    return False
            else:
                return False
    else:
        return False
    return True


if __name__ == '__main__':
    path1 = 'pieces_A.xml'
    path2 = 'pieces_AA.xml'
    with open(path1) as ff:
        xml = ff.read()
    with open(path2) as ff:
        xml2 = ff.read()
    res = compare_func(xml,xml2)
    print('result is ', res)