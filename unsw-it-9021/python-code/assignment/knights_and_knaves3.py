# @Time    : 2019-03-19 23:23
# @Author  : ZD Liu
import re
import sys
import copy

def read_text(path):
    with open(path, 'r') as f:
        text = f.read()
    return text

def split_text(text):
    cq = 0
    s = 0
    sent_list = []
    text = text.replace('\n', ' ')
    for i in range(len(text)):
        if text[i] == '"':
            cq += 1
            if cq % 2 == 0:
                str = text[s:].strip()
                if str[0].istitle() and not (str.startswith('Sir ') or str.startswith('Sirs ')):
                    sent_list.append(text[s:i + 1])
                    s = i + 1
        if cq % 2 == 0 and text[i] in ['.', '!', '?']:
            sent_list.append(text[s:i + 1])
            s = i + 1
        elif text[i - 1] in ['.', '!', '?']:
            sent_list.append(text[s:i + 1])
            s = i + 1
    return sent_list


def find_all_sris(sentence_list):
    avoid_cap_letters = ['I', 'Sir', 'Sirs', 'Knight', 'Knave', 'Knights', 'Knaves', 'At', 'All', 'Exactly', 'Should']
    sir_names = []
    for sentence in sentence_list:
        sentence = sentence.replace(',', ' ').replace('"', '').replace('.', '').replace('!', '').replace('?', '')
        word_list = re.split(' ', sentence.strip())
        for i in word_list[1:]:  # !!! error if the first word is name, there must be an error
            if i.istitle() and i not in avoid_cap_letters and i not in sir_names:
                sir_names.append(i)
    return sir_names


def quote_process(sir_names, sentence):
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
        if 'I' in said_list[1]:
            cont_people.extend(speaker)
            cont_people = list(set(cont_people))
        if 'us' in said_list[1]:
            cont_people.extend(sir_names)
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
    return solu_list


def sum_content(dic, cont_people):
    res = 0
    for i in cont_people:
        res += dic[i]
    return res


def solution_process(sir_names, sent_list, solu_table):
    res_table = solu_table
    q = 0
    for sentence in sent_list:
        if '"' not in sentence:
            continue
        q += 1
        print(q)
        speaker, cont_people = quote_process(sir_names, sentence)
        if speaker != '' and len(cont_people) > 0:
            if 'least one of' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) >= 1:
                            new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) == 0:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'least one of' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1 and sum_content(i, cont_people) >= 1 and sum_content(i,
                                                                                               cont_people) < len(
                            cont_people):
                        new_res.append(i)
                res_table = new_res
                continue
            if 'most one of' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) == 1:
                            new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) >= 2:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'most one of' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) >= len(cont_people) - 1:
                            if i not in new_res:
                                new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) <= len(cont_people) - 2:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'xactly one of' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) == 1:
                            new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) != 1:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'xactly one of' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1 and sum_content(i, cont_people) == len(cont_people) - 1:
                        # if sum_content(i, cont_people) ==  1:
                        new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) != len(cont_people) - 1:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'll of us' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) == len(cont_people):
                            new_res.append(i)
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) < len(cont_people):
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'll of us' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 0:
                        if sum_content(i, cont_people) > 0:
                            if i not in new_res:
                                new_res.append(i)
                res_table = new_res
                continue
            if 'I am a' in sentence and 'Knight' in sentence:
                res_table = res_table
                continue
            if 'I am a' in sentence and 'Knave' in sentence:
                res_table = []
                continue
            if ' or ' in sentence and 'Knight' in sentence:
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
                continue
            if ' or ' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1:
                        if sum_content(i, cont_people) < len(cont_people) and i not in new_res:
                            new_res.append(i)
                res_table = new_res
                continue
            if 'is a' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1 and sum_content(i, cont_people) == 1:
                        if i not in new_res:
                            new_res.append(i)
                    if i[speaker[0]] == 0 and sum_content(i, cont_people) == 0:
                        if i not in new_res:
                            new_res.append(i)
                res_table = new_res
                continue
            if 'is a' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1 and sum_content(i, cont_people) == 0:
                        if i not in new_res:
                            new_res.append(i)
                    if i[speaker[0]] == 0 and sum_content(i, cont_people) == 1:
                        if i not in new_res:
                            new_res.append(i)
                res_table = new_res
                continue
            if ' are ' in sentence and 'Knight' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 1 and sum_content(i, cont_people) == len(cont_people) and i not in new_res:
                        new_res.append(i)
                    if i[speaker[0]] == 0 and i not in new_res:
                        new_res.append(i)
                res_table = new_res
                continue
            if ' are ' in sentence and 'Knave' in sentence:
                new_res = []
                for i in res_table:
                    if i[speaker[0]] == 0 and i not in new_res and sum_content(i, cont_people) >= 1:
                        new_res.append(i)
                res_table = new_res
                continue
    return res_table


def print_res(lis, solution):
    lis.sort()
    print('The Sirs are:', ' '.join(lis))
    slt_count = len(solution)
    if slt_count < 1:
        print('There is no solution.')
    if slt_count == 1:
        print('There is a unique solution:')
        for i in range(len(lis)):
            if solution[0][lis[i]] == 1:
                print('Sir ' + lis[i] + ' is a Knight.')
            else:
                print('Sir ' + lis[i] + ' is a Knave.')
    if slt_count > 1:
        print('There are ' + str(slt_count) + ' solutions.')


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
        sir_names = find_all_sris(sent_list)
        solution_table = True_table(sir_names)
        solution = solution_process(sir_names, sent_list, solution_table)
        print_res(sir_names, solution)
