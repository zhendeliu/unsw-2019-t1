# EDIT THE FILE WITH YOUR SOLUTION

from bs4 import BeautifulSoup
from math import sqrt

def judge(corrd_dic):
    for i in range(len(corrd_dic)-3):
        value_list = []
        if corrd_dic[i][0]-corrd_dic[i+1][0] == 0:
            pass
        else:
            k = (corrd_dic[i][1] -corrd_dic[i+1][1]) / (corrd_dic[i][0] -corrd_dic[i+1][0])
            b = corrd_dic[i][1] - k*corrd_dic[i][0]
            for s in range(len(corrd_dic)-2):
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
    lis_location = [i for i in lis_location if i != ''] # and ' ' not in i
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


def available_coloured_pieces(file_open):
    text = file_open.read()
    soup = BeautifulSoup(text, 'xml')
    all_path = soup.find_all('path')
    all_dic = []
    for i in range(len(all_path)):
        str_loc = all_path[i].get('d')
        str_color = all_path[i].get('fill')
        corr_dic = get_corrd(str_loc)
        corr_dic['color'] = str_color
        if (len(corr_dic) < 3):
            return False ##### False 之后有错！
        all_dic.append(corr_dic)
    # !!! 需要判断不重复点的个数 如果小于2 则不能return！！！！
    return all_dic


def are_valid(coloured_pieces):
    res_lis = []
    for corr_dic in coloured_pieces:
        if judge(corr_dic):
            res_lis.append(1)
        else:
            res_lis.append(0)
    if sum(res_lis) == len(res_lis):
        return True
    else:
        return False

def edges_length(coor_pairs):
    lens_lis = []
    for i in range(len(coor_pairs)-2):
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

def catecorner_length(coor_pairs):
    lens_lis = []
    for i in range(len(coor_pairs)-2):
        j = i+2
        if j == len(coor_pairs)-1:
            j = 1
        lens = sqrt((coor_pairs[i][0] - coor_pairs[j][0]) ** 2 + (coor_pairs[i][1] - coor_pairs[j][1])**2)
        lens_lis.append(lens)
    return lens_lis

def are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces_2):
    edge_group1 = {}
    edge_group2 = {}
    for single in coloured_pieces_1:
        if len(single) in edge_group1.keys():
            edge_group1[len(single)].append(single)
        else:
            edge_group1[len(single)] = [single]
    for single2 in coloured_pieces_2:
        if len(single2) in edge_group2.keys():
            edge_group2[len(single2)].append(single2)
        else:
            edge_group2[len(single2)] = [single2]
    if list(edge_group1.keys()).sort() == list(edge_group2.keys()).sort():
        # print(edge_group1.keys())
        for key in edge_group1.keys():
            if key in edge_group2.keys() and len(edge_group1[key]) == len(edge_group2[key]):
                for k in range(len(edge_group1[key])):
                    e_lens1 = edges_length(edge_group1[key][k])

                    for p in range(len(edge_group2[key])):
                        e_lens2 = edges_length(edge_group2[key][p])
                        # print(edge_group1[key][k]['color'], edge_group2[key][p]['color'])
                        if compare_list(e_lens1,e_lens2) and edge_group1[key][k]['color'] ==edge_group2[key][p]['color']:
                            if len(e_lens2) ==3:
                                edge_group2[key].pop(p)
                                break
                            else:
                                con_lens1 = catecorner_length(edge_group1[key][k])
                                con_lens2 = catecorner_length(edge_group2[key][p])

                                if compare_list(con_lens1,con_lens2):
                                    edge_group2[key].pop(p)
                                    break
                                else:
                                    # print(1111111)
                                    return False
                if len(edge_group2[key]) != 0:
                    # print(222222)
                    return False
            else:
                # print(3333333)
                return False
    else:
        # print(4444444)
        return False
    return True

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computer_area(point_dic):
    area = 0
    for i in range(0, len(point_dic) - 2):
        p1 = Point(point_dic[i][0], point_dic[i][1])
        p2 = Point(point_dic[i+1][0], point_dic[i+1][1])
        triArea = (p1.x * p2.y - p2.x * p1.y) / 2
        area += triArea
    return abs(area)

def judge_areas(tangram, shape):
    area_sum = 0
    for piece in tangram:
        area_sum += computer_area(piece)
    shape_area = computer_area(shape[0])
    if area_sum == shape_area:
        return True
    else:
        return False

def computer_k_b(point1,point2):
    if point1[0] - point2[0] != 0:
        k = (point1[1] - point2[1]) / (point1[0] - point2[0])
        b = point1[1] - k * point1[0]
    else:
        k = 'vertical'
        b = point1[0]
    return k,b


# 计算是否相交 即计算各个图形的边（线段）是否相交（一条线段的顶点在另一条线段的两边，重合或者端点在线段上的均不算）
# 1.计算直线是否分割图形
# 2.如果分割，判断线段能否分割图形
# 3. 线段分割图形：与边相交斜率不等，斜率相等切有交点 判断是否分割了

# 1. 计算面积和是否相等
# 2. 判断所有图形是否在内部：pieces的坐标点都在图形内部，shape的顶点坐标不在任何pieces的内部
# 3. 判断有内部图形有无相交：判断pieces的坐标点是不是在彼此内部


#### 判断少于三条边的情况
def delete_ver(tangram):
    res_list = []
    a = []
    k_b_dic = {}
    for piece in tangram:
        edge_dic = {}
        for i in range(len(piece)-2):
            k,b = computer_k_b(piece[i],piece[i+1])
            edge_dic[i] = {}
            edge_dic[i]['k'] = k
            edge_dic[i]['b'] = b
            # edge_dic[i]['count'] = 1
            edge_dic[i]['start'] = piece[i]
            edge_dic[i]['end'] = piece[i+1]
            # edg_length = sqrt((piece[i][0] - piece[i+1][0]) ** 2 + (piece[i][1] - piece[i+1][1])**2)
            # edge_dic[i]['length'] = edg_length
            if (k,b) in a:
                pass
            else:
                a.append((k,b))
            if (k,b) in k_b_dic.keys():
                k_b_dic[(k,b)].append(edge_dic[i])
            else:
                k_b_dic[(k,b)] = [edge_dic[i]]
        res_list.append(edge_dic)
    res = {}
    for k_b in k_b_dic.keys():
        edge_len = 0
        point_list = []
        point_x_list = []
        point_y_list = []
        for edges in k_b_dic[k_b]:
            # for i in edges:
            if  edges['start'] not in point_list:
                point_list.append(edges['start'])
                point_x_list.append(edges['start'][0])
                point_y_list.append(edges['start'][1])
            if edges['end'] not in point_list:
                point_list.append(edges['end'])
                point_x_list.append(edges['end'][0])
                point_y_list.append(edges['end'][1])
        # point_list = sorted(list(set(point_list)))
        # 对点排序 从小到大
        point_list2 = []
        if k_b[0] == 'vertical' or k >0: # 根据y的值来排序
            point_y_list = sorted(list(set(point_y_list)))
            for i in point_y_list:
                for j in point_list:
                    if i == j[1]:
                        point_list2.append(j)
        else: # 根据x的值来排序
            point_x_list = sorted(list(set(point_x_list)))
            for i in point_x_list:
                for j in point_list:
                    if i == j[0]:
                        point_list2.append(j)

        for i in range(len(point_list2)-1):
            p = 0
            for edges in k_b_dic[k_b]:
                # for edge in edges:
                if (k=='vertical' or k > 0) and edges['start'][1] == point_list2[i][1] and edges['end'][1] >= point_list2[i+1][1]:
                    p += 1
                elif k <= 0 and edges['start'][0] == point_list2[i][0] and edges['end'][0] <= point_list2[i+1][0]:
                    p += 1
            if p == 1:
                if (k,b) in res.keys():
                    res[(k,b)].append([point_list[i],point_list[i+1]])
                else:
                    res[(k,b)] = [point_list[i],point_list[i+1]]
            elif p>2:
                print(2222222)
                return False
    return  res

def judgement(shape, remind_points):
    shape_k_b = {}
    for i in range(len(shape)-1):
        k, b = computer_k_b(shape[i], shape[i + 1])
        if (k,b) not in shape_k_b.keys():
            shape_k_b[(k,b)] = [[shape[i], shape[i + 1]]]
        else:
            shape_k_b[(k, b)].append([shape[i], shape[i + 1]])
    for k_b in shape_k_b.keys():
        all_lenth = 0
        for points in shape_k_b[k_b]:
            all_lenth += sqrt((points[i][0] - points[i+1][0]) ** 2 + (points[i][1] - points[i+1][1])**2)
        if k_b in remind_points.keys():
            all_lenth2 = 0
            for points in remind_points[k_b]:
                all_lenth2 += sqrt((points[i][0] - points[i + 1][0]) ** 2 + (points[i][1] - points[i + 1][1]) ** 2)
            if all_lenth != all_lenth2:
                print(3333333)
                return  False
        else:
            print(444444444)
            return False
    return True

def judgement2(tangram,shape):
    res_list = []
    a = []
    k_b_dic = {}
    tangram.extend(shape)
    for piece in tangram:
        edge_dic = {}
        for i in range(len(piece) - 2):
            k, b = computer_k_b(piece[i], piece[i + 1])
            edge_dic[i] = {}
            edge_dic[i]['k'] = k
            edge_dic[i]['b'] = b
            # edge_dic[i]['count'] = 1
            edge_dic[i]['start'] = piece[i]
            edge_dic[i]['end'] = piece[i + 1]
            # edg_length = sqrt((piece[i][0] - piece[i+1][0]) ** 2 + (piece[i][1] - piece[i+1][1])**2)
            # edge_dic[i]['length'] = edg_length
            if (k, b) in a:
                pass
            else:
                a.append((k, b))
            if (k, b) in k_b_dic.keys():
                k_b_dic[(k, b)].append(edge_dic[i])
            else:
                k_b_dic[(k, b)] = [edge_dic[i]]
        res_list.append(edge_dic)
    for k_b in k_b_dic.keys():
        if len(k_b_dic[k_b]) <2:
            return False
    return True
    #
    # return k_b_dic



def is_solution(tangram,shape):
    if judge_areas(tangram,shape):
        return judgement2(tangram,shape)
    else:
        return False




if __name__ == '__main__':
    # third question
    file = open('shape_A_1.xml')
    shape = available_coloured_pieces(file)
    # file = open('tttttest.xml')
    file = open('tangram_A_1_b.xml')
    tangram = available_coloured_pieces(file)
    print(is_solution(tangram, shape))
    file = open('tangram_A_2_a.xml')
    tangram = available_coloured_pieces(file)
    print(is_solution(tangram, shape))

    # file = open('pieces_A.xml')
    # # file = open('incorrect_pieces_4.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    # file = open('pieces_AA.xml')
    # # file = open('incorrect_pieces_4.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    # file = open('incorrect_pieces_1.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    # file = open('incorrect_pieces_2.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    # file = open('incorrect_pieces_3.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    # file = open('incorrect_pieces_4.xml')
    # coloured_pieces = available_coloured_pieces(file)
    # print(are_valid(coloured_pieces))
    #
    # # second question
    # file = open('pieces_A.xml')
    # coloured_pieces_1 = available_coloured_pieces(file)
    # # print(coloured_pieces_1)
    # file = open('pieces_AA.xml')
    # coloured_pieces_2 = available_coloured_pieces(file)
    # # print(coloured_pieces_2)
    # print(are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2))
    # file = open('shape_A_1.xml')
    # coloured_pieces_2 = available_coloured_pieces(file)
    # # print(coloured_pieces_2)
    # print(are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2))


