#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-19 23:23
# @Author  : ZD Liu



import re
import sys
import copy

def read_text(path):
    with open(path,'r') as f:
        text = f.read()
    return text

# def split_text(text):
#     text = text.replace('\n',' ')
#     # A sentence starts with a capital letter and ends in a full stop, an exclamation\\
#     # mark, or a question mark, possibly followed by closing double quotes.
#     sent_list = [text]
#
#     for i in ['. ','! ','? ','."','!"','?"']:
#         new_list = []
#         for sentence in sent_list:
#             lis = []
#             s = sentence.split(i)
#             for q in range(len(s)):
#                 if q == len(s)-1 and len(s[q]) > 1:
#                     lis.append(s[q])
#                 elif len(s[q]) > 1:
#                     lis.append(s[q] + i)
#             new_list.extend(lis)
#         sent_list = new_list
#     # sent_list = re.split('[.!?]',text) # ！！！！！
#     return sent_list


def split_text(text):
    cq = 0
    s = 0
    sent_list = []
    text = text.replace('\n',' ')
    for i in range(len(text)):
        if text[i] == '"':
            cq += 1
            if i < len(text)-3 and cq % 2 == 0 and (text[i+1].istitle() or text[i+2].istitle() or text[i+3].istitle()):
                sent_list.append(text[s:i + 1])
                s = i + 1
        if cq % 2 == 0 and text[i] in ['.', '!', '?']:
            sent_list.append(text[s:i+1])
            s = i+1


    return sent_list
# def split_text(text):
#     text = text.replace('\n',' ')
#     # A sentence starts with a capital letter and ends in a full stop, an exclamation\\
#     # mark, or a question mark, possibly followed by closing double quotes.
#     sent_list = []
#     sp = []
#     if '"' in text:
#         res_split = text.split('"')
#         print(len(res_split))
#         for i in range(len(res_split)):
#             print(i)
#             if i % 2 == 0:
#                 sp = re.split('[.!?]',res_split[i])
#                 if len(sp) < 1  or sp[0] == ' ':
#                     continue
#                 if i == len(res_split)-1:
#                     sp[-1] = sp[-1] + '.'
#             if (i % 2 == 1 or i == len(res_split)-1) and sp[-1] != '' and '.' not in sp[-1] :
#                     res_split[i] = sp[-1] + '"' + res_split[i] + '"'
#                     sp.pop(-1)
#                     sent_list.append(res_split[i])
#                     sent_list.extend(sp)
#             elif (i % 2 == 1 or i == len(res_split)-1) and sp[-1] != '' and '.' not in sp[0] :
#                     res_split[i-1] = '"' + res_split[i-1] + '"' + sp[0]
#                     sp.pop(0)
#                     sent_list.append(res_split[i-1])
#                     sent_list.extend(sp)
#
#     return sent_list

def find_all_sris(sentence_list):
    avoid_cap_letters = ['I','Sir','Sirs','Knight','Knave','Knights','Knaves','At','All','Exactly','Should']
    sir_names = []
    for sentence in sentence_list:
        sentence = sentence.replace(',',' ').replace('"','').replace('.','').replace('!','').replace('?','')
        word_list = re.split(' ',sentence.strip())
        for i in word_list[1:]: # !!! error if the first word is name, there must be an error
            if i.istitle() and i not in avoid_cap_letters and i not in sir_names:
                sir_names.append(i)
    # print(len(sir_names))
    return sir_names

def quote_process(sentence):
    speaker = ''
    cont_people = []
    if '"' in sentence:
        said_list = sentence.split('"')
        speaker = find_all_sris([said_list[0]])
        if len(speaker) > 0:
            pass
        else:
            speaker = find_all_sris([said_list[2]])
        cont_people = find_all_sris([said_list[1]])
        if 'I' in said_list[1] or 'us' in said_list[1]:
            cont_people.extend(speaker)
            cont_people = list(set(cont_people))
    return speaker, cont_people

def True_table(lis):
    res_dic = {}
    solu_list = []

    for i in lis:
        res_dic[i] = 1
    solu_list.append(res_dic)
    i = 0
    while i < len(lis):
        lis2 = []
        for dic in solu_list:
            dic2 = copy.copy(dic)
            dic2[lis[i]] = 0
            lis2.append(dic2)
        solu_list.extend(lis2)
        i += 1
    # print(len(solu_list))
    return solu_list

def sum_content(dic, cont_pepple):
    res = 0
    for i in cont_pepple:
        res+= dic[i]
    return  res


def solution_process(sent_list, solu_table):
    dic_quote_sentence = {}
    dic_quote_sentence[1] = 'least one of'
    dic_quote_sentence[2] = 'most one of'
    dic_quote_sentence[3] = 'exactly one of'
    dic_quote_sentence[4] = 'all of us'
    dic_quote_sentence[5] = 'I am a'
    dic_quote_sentence[6] = 'Sir Sir_Name is a'
    dic_quote_sentence[7] = 'or'
    dic_quote_sentence[8] = 'are'
    dic_quote_sentence[9] = 'Knight'
    dic_quote_sentence[10] = 'Knave'
    res_table = solu_table
    for sentence in sent_list:
        if '"' not in sentence:
            continue
        speaker, cont_people = quote_process(sentence)
        if speaker != '' and len(cont_people) > 0:
            if dic_quote_sentence[1] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 :
                            if sum_content(i, cont_people) >= 1:
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) == 0:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[1] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 and sum_content(i, cont_people) >= 1 and sum_content(i,cont_people)< len(cont_people):
                            new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[2] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 :
                            if sum_content(i, cont_people) == 1:
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) >= 2:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[2] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 :
                            if sum_content(i, cont_people) >= len(cont_people)-1:
                                if i not in new_res:
                                    new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i,cont_people) <= len(cont_people) -2:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res

            if dic_quote_sentence[3] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 :
                            if sum_content(i, cont_people) == 1:
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) != 1 :
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[3] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 :
                            if sum_content(i, cont_people) == len(cont_people)- 1:
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) <= len(cont_people) -2 :
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[4] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1:
                            if sum_content(i, cont_people) == len(cont_people):
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) < len(cont_people) :
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res

            if dic_quote_sentence[4] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) > 0:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[5] in sentence and dic_quote_sentence[9] in sentence:
                res_table = res_table
            if dic_quote_sentence[5] in sentence and dic_quote_sentence[10] in sentence:
                res_table = []
            if dic_quote_sentence[6] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        for others in cont_people:
                            if i[speaker[0]] == 1 and i[others] == 1:
                                if i not in new_res:
                                    new_res.append(i)
                            if i[speaker[0]] == 0 and i[others] == 0:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[6] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        for others in cont_people:
                            if i[speaker[0]] == 1 and i[others] == 0:
                                if i not in new_res:
                                    new_res.append(i)
                            if i[speaker[0]] == 0 and i[others] == 1:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[7] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1:
                            if i not in new_res:
                                new_res.append(i)
                        if i[speaker[0]] == 0:
                            if sum_content(i, cont_people) < 1:
                                if i not in new_res:
                                    new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[7] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1:
                            if sum_content(i, cont_people) < len(cont_people) and i not in new_res:
                                new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[8] in sentence and dic_quote_sentence[9] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 1 and sum_content(i, cont_people) == len(cont_people) and i not in new_res:
                            new_res.append(i)
                        if i[speaker[0]] == 0 and i not in new_res:
                            new_res.append(i)
                    res_table = new_res
            if dic_quote_sentence[8] in sentence and dic_quote_sentence[10] in sentence:
                if speaker[0] in cont_people:
                    new_res = []
                    for i in res_table:
                        if i[speaker[0]] == 0 and i not in new_res and sum_content(i, cont_people) >= 1:
                            new_res.append(i)
                    res_table = new_res
    return  res_table


def print_res(lis,solution):
    # lis[names***]
    # dic{'name':k***}
    lis.sort()
    print('The Sirs are:', ' '.join(lis))
    slt_count = len(solution)
    if slt_count < 1:
        print('There is no solution.')
    if slt_count == 1:
        print('There is a unique solution:')
        for i  in range(len(lis)):
            if solution[0][lis[i]] == 1:
                print('Sir '+lis[i]+' is a Knight.')
            else:
                print('Sir '+lis[i]+' is a Knave.')
    if slt_count > 1:
        print('There are ' + str(slt_count) +' solutions.')

if __name__ == '__main__':
    from pathlib import Path
    file_name = input('Which text file do you want to use for the puzzle? ')
    file_path = Path(file_name)
    if not file_name.endswith('.txt'):
        print('Incorrect input, giving up.')
        sys.exit()
    elif not file_path.exists():
        print('Incorrect input, giving up.')
        sys.exit()
    else:
        text = read_text(file_path)
        sent_list = split_text(text)
        sir_names = find_all_sris(sent_list) # should not process text directly
        solution_table = True_table(sir_names)
        solution = solution_process(sent_list , solution_table)
        print_res(sir_names,solution)
