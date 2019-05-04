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



def computer_not_join3(points_list1,points_list2):
    # 判断边是否相交 求出交点
    # 判断
    return


def computer_not_join(points_list1,points_list2):
    for i in range(len(points_list1)-2):
        # print(points_list1[i])
        k1, b1 = computer_k_b(points_list1[i], points_list1[i + 1])
        if k1 == 'vertical':
            for j in range(len(points_list2)-2):
                if points_list2[j][0] >= b1 and  points_list2[j + 1][0]>= b1:
                    continue
                elif points_list2[j][0] <= b1 and  points_list2[j + 1][0]<= b1:
                    continue
                else:
                    k2, b2 = computer_k_b(points_list2[j], points_list2[j + 1])
                    if k1 == k2:
                        continue
                    else:
                        # if k2 == 'vertical':
                        #     if points_list1[i][0] >= b1 and points_list1[i + 1][0] >= b1:
                        #         continue
                        #     elif points_list1[i][0] <= b1 and points_list2[i + 1][0] <= b1:
                        #         continue
                        #     else:
                        #         print(11111)
                        #         return False
                        # else:
                        tof = (points_list1[i][1] - k2 * points_list1[i][0] - b2)
                        tof2 = (points_list1[i + 1][1] - k2 * points_list1[i + 1][0] - b2)
                        if (tof >0 and tof2 >0) or (tof <0  and tof2<0) or tof == 0 or tof2 == 0 :
                            continue
                        else:
                            # print(points_list1[i],points_list1[i+1],points_list2[j], points_list2[j + 1])
                            print(22222)
                            return False
                    # return False
        else:
            for j in range(len(points_list2)-2):
                k2, b2 = computer_k_b(points_list2[j], points_list2[j + 1])
                if k1 == k2:

                    continue
                else:
                    tof = (points_list2[j][1] - k1 * points_list2[j][0] - b1)
                    tof2 = (points_list2[j+1][1] - k1 * points_list2[j+1][0] - b1)
                    if (tof > 0 and tof2 > 0) or (tof < 0 and tof2 < 0) or tof == 0 or tof2 == 0:
                        continue
                    elif k2 == 'vertical':
                        if points_list1[i][0] >= b2 and points_list1[i + 1][0] >= b2:
                            continue
                        elif points_list1[i][0] <= b2 and points_list2[i + 1][0] <= b2:
                            continue
                        else:
                            print(33333)
                            return False
                    else:
                        tof = (points_list1[i][1] - k2 * points_list1[i][0] - b2)
                        # print(points_list1[i])
                        tof2 = (points_list1[i + 1][1] - k2 * points_list1[i + 1][0] - b2)
                        if (tof > 0 and tof2 > 0) or (tof < 0 and tof2 < 0) or tof == 0 or tof2 == 0:
                            continue
                        else:
                            return False
    return True










def computer_not_join2(points_list1,points_list2, shape = 0):
    for i in range(len(points_list1)-2):
        k1, b1 = computer_k_b(points_list1[i], points_list1[i + 1])
        if k1 == 'vertical':
            join_points = []
            if len(join_points) == 2:
                print(101202020)
            for j in range(len(points_list2)-2):

                if points_list2[j][0] >= b1 and  points_list2[j + 1][0]>= b1:
                    if points_list2[j][0] == b1 and points_list2[j+1][0] != b1 and points_list2[j][0] not in join_points:
                        join_points.append(points_list1[i])
                    if points_list2[j+1][0] == b1 and points_list2[j][0] != b1 and points_list2[j+1][0] not in join_points:
                        join_points.append(points_list1[i+1])
                    continue
                elif points_list2[j][0] <= b1 and  points_list2[j + 1][0]<= b1:
                    if points_list2[j][0] == b1 and points_list2[j+1][0] != b1 and points_list2[j][0] not in join_points:
                        join_points.append(points_list1[i])
                    if points_list2[j+1][0] == b1 and points_list2[j][0] != b1 and points_list2[j+1][0] not in join_points:
                        join_points.append(points_list2[i+1])
                    continue
                else:
                    k2, b2 = computer_k_b(points_list2[j], points_list2[j + 1])
                    # if k1 == k2: # 不会发生
                    #     continue
                    # else:
                    tof = (points_list1[i][1] - k2 * points_list1[i][0] - b2)
                    tof2 = (points_list1[i + 1][1] - k2 * points_list1[i + 1][0] - b2)
                    if (tof >0 and tof2 >0) or (tof <0  and tof2<0) or tof == 0 or tof2 == 0 :
                        btw = int(points_list1[i][0] <= points_list2[j][0]) + int(
                            points_list1[i + 1][0] <= points_list2[j][0])
                        if tof == 0 and tof2 != 0 and btw==1 and points_list1[i] not in points_list2.values():
                            join_points.append(points_list1[i])
                        btw = int(points_list1[i][0] <= points_list2[j + 1][0]) + int(
                            points_list1[i + 1][0] <= points_list2[j + 1][0])
                        if tof2 == 0 and tof != 0 and btw==1 and points_list1[i] not in points_list2.values():
                            join_points.append(points_list1[i + 1])
                        continue
                    else:
                        # print(points_list1[i],points_list1[i+1],points_list2[j], points_list2[j + 1])
                        print(22222)
                        return False
                    # return False
            if len(join_points) >= 2 and not shape:
                # 判断能否分割
                value_list = []
                for j in range(len(points_list2) - 2):
                    if points_list2[j][0] >= b1:
                        value_list.append(1)
                    if points_list2[j][0] <= b1:
                        value_list.append(0)
                if sum(value_list) == 0 or sum(value_list) == len(value_list):
                    pass
                else:
                    print(77777)
                    return False
        else:
            join_points = []
            for j in range(len(points_list2)-2):
                k2, b2 = computer_k_b(points_list2[j], points_list2[j + 1])
                if k1 != k2:
                    tof = (points_list2[j][1] - k1 * points_list2[j][0] - b1)
                    tof2 = (points_list2[j+1][1] - k1 * points_list2[j+1][0] - b1)
                    if (tof > 0 and tof2 > 0) or (tof < 0 and tof2 < 0) or tof == 0 or tof2 == 0:
                        btw = int(points_list1[i][0] <= points_list2[j][0]) + int(points_list1[i+1][0] <= points_list2[j][0])
                        if tof == 0 and tof2 != 0 and btw==1 and points_list1[i] not in join_points :
                            join_points.append(points_list1[i])
                            continue
                        btw = int(points_list1[i][0] <= points_list2[j+1][0]) + int(points_list1[i + 1][0] <= points_list2[j+1][0])
                        if tof2 == 0 and tof != 0 and btw==1 and points_list1[i+1] not in join_points :
                            join_points.append(points_list1[i+1])
                            continue
                    elif k2 == 'vertical':
                        if points_list1[i][0] >= b2 and points_list1[i + 1][0] >= b2:
                            if points_list1[i][0] == b2 and points_list1[i][0] != b2 and points_list1[i] not in join_points:
                                join_points.append(points_list1[i])
                            if points_list1[i][0] != b2 and points_list1[i+1][0] == b2 and points_list1[i+1] not in join_points:
                                join_points.append(points_list1[i + 1])
                            continue
                        elif points_list1[i][0] <= b2 and points_list2[i + 1][0] <= b2:
                            if points_list1[i][0] == b2 and points_list1[i][0] != b2 and points_list1[i] not in join_points:
                                join_points.append(points_list1[i])
                            if points_list1[i][0] != b2 and points_list1[i+1][0] == b2 and points_list1[i+1] not in join_points:
                                join_points.append(points_list1[i + 1])
                            continue
                        else:
                            print(33333)
                            return False
                    else:
                        tof = (points_list1[i][1] - k2 * points_list1[i][0] - b2)
                        # print(points_list1[i])
                        tof2 = (points_list1[i + 1][1] - k2 * points_list1[i + 1][0] - b2)
                        if (tof > 0 and tof2 > 0) or (tof < 0 and tof2 < 0) or tof == 0 or tof2 == 0:
                            if tof == 0 and tof2 != 0 and points_list1[i] not in join_points:
                                join_points.append(points_list1[i])
                            if tof2 == 0 and tof != 0 and points_list1[i+1] not in join_points:
                                join_points.append(points_list1[i + 1])
                            continue
                        else:
                            print(4444)
                            return False
            if len(join_points) >= 2 and not shape:
                # 判断能否分割
                value_list = []

                for j in range(len(points_list2) - 2):
                    print(points_list1[i])
                    print(k1,b1)

                    print(points_list2[j])
                    value_list.append(int(points_list2[j][1] - k1 * points_list2[j][0] - b1 < 0))
                print(len(points_list2))
                print(value_list)
                if sum(value_list) == 0 or sum(value_list) == len(value_list):
                    pass
                else:
                    print(5555)
                    return False
    return True