import sys
import os
import re
import itertools
from pathlib import Path


# 真值表
def set_truth_table(sirs_name):
    number_of_sirs = len(sirs_name)
    possible_solu = list(itertools.product([0, 1], repeat=number_of_sirs))
    truth_table = []
    for i in range(len(possible_solu)):
        temp_dic = {}
        for j in range(number_of_sirs):
            temp_dic[sirs_name[j]] = possible_solu[i][j]
        truth_table.append(temp_dic)
    return truth_table


test_file = Path(input('Which text file do you want to use for the puzzle? '))

if not os.path.exists(test_file):
    print(f'There is no file named {test_file} in the working directory, giving up...')
    sys.exit()
with open(test_file, 'r') as file:

    content = file.read()
    content = content.replace('\n', ' ')
    content = content.replace('!"', '"!')
    content = content.replace('."', '".')
    content = content.replace('.', '. ')

    # sentence_content 按照标点符号断开，储存完整的句子
    sentence_content = re.split(r'[.?!]', content)

    # 删除每个句子的前后空格
    for i in range(len(sentence_content)):
        sentence_content[i] = sentence_content[i].strip()

    # 删除sentence_content列表中的空元素 [''] or [' ']
    while '' in sentence_content:
        sentence_content.remove('')
    while ' ' in sentence_content:
        sentence_content.remove(' ')

    # list_content 储存每个单词，用来寻找大写的单词
    list_content = content.split(' ')

    # 删除list_content 单词前后的标点符号
    for i in range(len(list_content)):
        list_content[i] = list_content[i].replace('!', '')
        list_content[i] = list_content[i].replace('?', '')
        list_content[i] = list_content[i].replace('"', '')
        list_content[i] = list_content[i].replace(',', '')
        list_content[i] = list_content[i].replace(':', '')
        list_content[i] = list_content[i].replace('.', '')

    # 删除list_content列表中的空元素 [''] or [' ']
    while '' in list_content:
        list_content.remove('')
    while ' ' in list_content:
        list_content.remove(' ')

    # capital_content 空list，通过遍历list_content,找到所有的首字母大写的单词
    capital_content = []

    # 遍历list_content 提取出所有的首字母大写的单词，添加到capital_list中
    for i in range(len(list_content)):
        if list_content[i].istitle():
            capital_content.append(list_content[i])

    # 定义normal_capital 储存常见的大写单词
    normal_capital = ['Sir', 'Sirs', 'Knight', 'Knave', 'Knights', 'Knaves', 'I']

    # sirs_name 储存sir的名字
    sirs_name = []

    # 提取每个句子的第一个单词(首字母为大写)，并添加到normal_capital列表中
    for i in range(len(sentence_content)):
        normal_capital.append((sentence_content[i].split())[0])

    for i in range(len(normal_capital)):
        normal_capital[i] = normal_capital[i].replace('!', '')
        normal_capital[i] = normal_capital[i].replace(',', '')
        normal_capital[i] = normal_capital[i].replace('.', '')
        normal_capital[i] = normal_capital[i].replace('"', '')
        normal_capital[i] = normal_capital[i].replace('?', '')

    # 找出capital_word列表中 不存在于 normal_capital列表中的元素 （可能会有重复的元素）
    for capital_word in capital_content:
        if capital_word not in normal_capital:
            sirs_name.append(capital_word)

    # 去掉sirs_name列表中 重复的元素
    distinct_sirs_name = sorted(list(set(sirs_name)))
    print(f'The Sirs are: ', end='')
    for i in range(len(distinct_sirs_name) - 1):
        print(distinct_sirs_name[i],end=' ')
    print(distinct_sirs_name[-1])


# proof_1{sir:[sir说的话]}
# def extract_proof(sentence_content, distinct_sirs_name):
    proof_1 = {}
    proof_2 = {}
    for i in range(len(sentence_content)):
        if '"' in sentence_content[i]:
            speaker_1 = re.findall(r'[\S\w\s]*\s\"', sentence_content[i])
            says = re.findall(r'\"[\w\s\S]*\S\"', sentence_content[i])
            speaker_2 = re.findall(r'\"\s[\w\s]*', sentence_content[i])
            str_says_1 = str(says).replace("['", '')
            str_says = str(str_says_1).replace("']", '')
            for people in distinct_sirs_name:
                if people in ''.join(speaker_1):
                    if people not in proof_1.keys():
                        proof_1[people] = []
                        proof_1[people].append(str_says)
                    else:
                        proof_1[people].append(str_says)
                elif people in ''.join(speaker_2):
                    if people not in proof_1.keys():
                        proof_1[people] = []
                        proof_1[people].append(str_says)
                    else:
                        proof_1[people].append(str_says)

    # proof_2{sir:[说的话中提及的人]}
    judge_table = set_truth_table(distinct_sirs_name)
    for people in proof_1.keys():
        for w in range(len(proof_1[people])):
            proof_2[people] = []
            str_proof_1_values = proof_1[people][w]
            for sir in distinct_sirs_name:
                if sir in str_proof_1_values:
                    proof_2[people].append(sir)
            if 'I ' in str_proof_1_values:
                proof_2[people].append(people)
            if ' us ' in str_proof_1_values:
                for sir in distinct_sirs_name:
                    proof_2[people].append(sir)

            #  判断各种情况
            if 'least one of' in str_proof_1_values and 'Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s >= 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == 0:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'least one of' in str_proof_1_values and 'Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s <= len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'most one of' in str_proof_1_values and 'Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s <= 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s > 1:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'most one of' in str_proof_1_values and 'Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s >= len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s < len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'xactly one of' in str_proof_1_values and 'Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != 1:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'xactly one of' in str_proof_1_values and 'Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'll of us' in str_proof_1_values and 'Knights' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    s = 0
                    if judge_table[i][people] == 1:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'll of us' in str_proof_1_values and 'Knaves' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    s = 0
                    if judge_table[i][people] == 1:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == 0:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != 0:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'I am a Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'I am a Knave' in str_proof_1_values:
                judge_table = []
                continue

            if 'Sir' in str_proof_1_values and 'or' in str_proof_1_values and 'is a Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s >= 1:
                            comp_truth_table.append(judge_table[i])

                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == 0:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue
            if 'Sir' in str_proof_1_values and 'or' in str_proof_1_values and 'is a Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s <= len(proof_2[people]) - 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        s = 0
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'Sir' in str_proof_1_values and 'is a Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        if judge_table[i][proof_2[people][0]] == 1:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        if judge_table[i][proof_2[people][0]] == 0:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'Sir' in str_proof_1_values and 'is a Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    if judge_table[i][people] == 1:
                        if judge_table[i][proof_2[people][0]] == 0:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        if judge_table[i][proof_2[people][0]] == 1:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'are Knight' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    s = 0
                    if judge_table[i][people] == 1:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != len(proof_2[people]):
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

            if 'are Knave' in str_proof_1_values:
                comp_truth_table = []
                for i in range(len(judge_table)):
                    s = 0
                    if judge_table[i][people] == 1:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s == 0:
                            comp_truth_table.append(judge_table[i])
                    if judge_table[i][people] == 0:
                        for name in proof_2[people]:
                            s += judge_table[i][name]
                        if s != 0:
                            comp_truth_table.append(judge_table[i])
                judge_table = comp_truth_table
                continue

    # 判断judge_table的长度 ，根据长度判断solution的个数，并输出
    if len(judge_table) == 0:
        print('There is no solution.')
    if len(judge_table) > 1:
        print(f'There are {len(judge_table)} solutions.')
    if len(judge_table) == 1:
        print('There is a unique solution:')
        for sir in distinct_sirs_name:
            if judge_table[0][sir] == 1:
                judge_table[0][sir] = 'Knight'
            if judge_table[0][sir] == 0:
                judge_table[0][sir] = 'Knave'
        for sir in distinct_sirs_name:
            print(f'Sir {sir} is a {judge_table[0][sir]}.')


