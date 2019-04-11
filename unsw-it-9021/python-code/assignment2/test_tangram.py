#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-06 10:19
# @Author  : ZD Liu


# first task:您必须检查.xml文件中表示的片段是否满足我们的约束。因此，您必须检查每个部分是否为凸面，如果它表示具有n个边（n≥3）的多边形，则表示由n个顶点的枚举组成，顺时针或逆时针。
# 与碎片相反，形状不被认为是凸多边形。仍然假设它们是简单的多边形（简单多边形的边界不会交叉自身;特别是，它不能由至少2个多边形组成，这些多边形通过让它们中的两个在它们的一个顶点处彼此“接触”而连接起来-eg，两个矩形，使得一个矩形的右上角是另一个矩形的左下角;这是不允许的）。
# second task:您必须检查两个.xml文件中表示的片段集是否相同，允许片段翻转并允许不同的方向。
# third task:您必须检查.xml文件中表示的片段是否是所代表的七巧板拼图的解决方案在另一个.xml文件中
# 坐标是非负整数
# 坐标是非负整数。这意味着我们考虑的那些套件排除了传统的七巧板游戏，其中√2随处可见......
# 我们要求每件都是凸多边形。 .xml文件应通过n对坐标的枚举表示具有n个边（n≥3）的块，连续顶点的坐标，第一个顶点是任意的，并且枚举是顺时针或逆时针。
# 这些碎片可以有不同的方向并翻转
from bs4 import BeautifulSoup
import numpy as np

### first task 判断凸边形，所有内角小于 180 度
def judge(corrd_dic):
    for i in range(len(corrd_dic)-1):
        # 以point2为基础 decide point3 的角度 涉及到 p21和p23的角度大于p12和p24的角度
        value_list = []
        print(corrd_dic[i][0], corrd_dic[i+1][0])
        if corrd_dic[i][0]-corrd_dic[i+1][0] == 0:
            pass
        else:
            k = (corrd_dic[i][1] -corrd_dic[i+1][1]) / (corrd_dic[i][0] -corrd_dic[i+1][0])
            b = corrd_dic[i][1] - k*corrd_dic[i][0]
            for s in corrd_dic:
                if s == i or s == i+1 :
                    pass
                else:
                    v = (corrd_dic[s][1] - k * corrd_dic[s][0] - b) > 0
                    value_list.append(int(v))
            if sum(value_list) == 0 or sum(value_list) == len(value_list):
                pass
            else:
                return False
    return True

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
        # elif 'Z' in lis_location[lo].upper():
        #     coordinate_pair[i] = [int(lis_location[1]),int(lis_location[2])]
    return coordinate_pair


def judge_each_path(text):
    soup = BeautifulSoup(text, 'xml')
    all_path = soup.find_all('path')
    res_lis = []
    for i in range(len(all_path)):
        str_loc = all_path[i].get('d')
        corr_dic = get_corrd(str_loc)
        if judge(corr_dic):
            res_lis.append(1)
        else:
            res_lis.append(0)
    return res_lis

def available_coloured_pieces(text):
    judge_res = judge_each_path(text)
    if sum(judge_res) == len(judge_res):
        return True
    else:
        return False


if __name__ == '__main__':
    path = 'tangram_A_2_a.xml'
    with open(path) as ff:
        xml = ff.read()
    res = available_coloured_pieces(xml)
    print('result is ', res)