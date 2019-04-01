import sys
import re
import copy

def find_names(text):
    text = text.replace('\n', ' ')
    text = text.replace('."', '".')
    text = text.replace('!"', '"!')
    text = text.replace(',"', '",')
    text = text.replace('?"', '"?')
    text = text.replace('.', '. ')
    text = text.split(' ')
    # 删除list_content列表中的空元素 [''] or [' ']
    while '' in text:
        text.remove('')
    while ' ' in text:
        text.remove(' ')
    #找到！和.后面的单词，因为后面的单词首字母是大写的
    ordinary_words = ['Sirs','Sir','Knight','Knights','Knave','Knaves','I','Should','Then']
    for i in range(len(text) - 2):
        if len(text[i]) < 1:
            continue
        if text[i][-1] == '!':
            ordinary_words.append(text[i + 1])
        a = text[i]
        if text[i][-1] == '.':
            ordinary_words.append(text[i + 1])
        if text[i] in ordinary_words:
            ordinary_words.append(text[i])
        if text[i][0] == '"':
            text_begin = text[i].replace('"','')
            ordinary_words.append(text_begin)
    #找到全部首字母大写的单词
    capital_words = []
    for i in range(len(text)):
        text[i] = text[i].strip()
    for i in range(1, len(text)):
        if len(text[i]) < 1:
            continue
        if ord(text[i][0]) >= 65 and ord(text[i][0]) <= 90:
            capital_words.append(text[i])

    sirs_names = []
    capital_words2 = []
    for i in range(len(capital_words)):
        if capital_words[i] not in ordinary_words:
            capital_words2.append(capital_words[i])
    capital_words = capital_words2
    #去掉每个单词前后可能出现的标点
    for i in range(len(capital_words)):
        capital_words[i] = capital_words[i].replace('!', '')
        capital_words[i] = capital_words[i].replace(',', '')
        capital_words[i] = capital_words[i].replace('.', '')
        capital_words[i] = capital_words[i].replace('"', '')
        capital_words[i] = capital_words[i].replace('?', '')
    #找到人名
    sirs_names = []
    for i in range(len(capital_words)):
        if capital_words[i] not in ordinary_words:
            sirs_names.append(capital_words[i])
    # 去掉sirs_name列表中 重复的元素
    sirs_names = list(set(sirs_names))
    sirs_names.sort()
    return  sirs_names

def ture_or_false(sirs_names):
    # 制作真值表
    sirs_number = int(len(sirs_names))
    ex_list = []
    t_or_f = []
    for i in range(0, 2 ** sirs_number):
        ex_list.append(f'{i:0b}')
    for i in range(2 ** sirs_number):
        t_or_f.append(ex_list[i].zfill(sirs_number))
    return  t_or_f

#找speaker，说话的人，说的话，以及将人设置为key，说的话赋值value，形成字典
def create_zd(text,sirs_names):
    zd = {}
    text = text.replace('\n', ' ')
    text = text.replace('."', '".')
    text = text.replace('!"', '"!')
    text = text.replace('?"', '"?')
    text = re.split('[.!?]',text)
    new_text = []

    for i in text:
        if '"' in i:
            new_text.append(i)
    for i in new_text:
        i = i.strip()
        i = i.split(' ')
        speaker_sentence = []
        if i[0][0] == '"':
            for j in range(len(i)):
                if i[j][-1] == '"':
                    for k in range(j + 1, len(i)) :
                        if i[k] in sirs_names:
                            for n in range(0, j + 1):
                                speaker_sentence.append(i[n])
                            if i[k] in zd.keys():
                                zd[i[k]].append(' '.join(speaker_sentence))
                            else:
                                zd[i[k]] = [' '.join(speaker_sentence)]
        if i[0] != '"':
            for j in range(1, len(i)):
                if len(i[j]) < 1:
                    continue
                if i[j][0] == '"':
                    for k in range(j + 1, len(i)):
                        if len(i[k]) < 1:
                            continue
                        if i[k][-1] == '"':
                            for n in range(j, k + 1):
                                speaker_sentence.append(i[n])
                    for p in range(0, j):
                        if i[p] in sirs_names:
                            if i[p] in zd.keys():
                                zd[i[p]].append(' '.join(speaker_sentence))
                            else:
                                zd[i[p]] = [' '.join(speaker_sentence)]
    return zd

def decide(sirs_names, zd):
    #将说的话拆分成三个部分，涉及到的人，说话类型，及是knight还是knave
    t_or_f = ture_or_false(sirs_names)

    new_zd = {}
    for i in zd.keys():
        for k in zd[i]:
            inside_sirs = []
            inside_role = []
            k = k.replace('"', '')
            new_value = k.split(' ')

            for n in range(1, len(new_value) - 1):
                if len(new_value[n]) < 1:
                    continue
                if ord(new_value[n][0]) >= 65 and ord(new_value[n][0]) <= 90:
                    if new_value[n] == 'I':
                        new_value[n] = i
                    if new_value[n] != 'Sir' and new_value[n] != 'Sirs':
                        inside_sirs.append(new_value[n].replace(',',''))

                if new_value[n] == 'us':
                    inside_sirs = copy.copy(sirs_names)
            new_value_clean = new_value[-1].replace(',','')
            inside_role.append(new_value_clean)
            inside_sirs.extend(inside_role)
            new_zd[i] = inside_sirs

            #开始分情况判定
            temp_t_f = []

            if 'least one of us' in k:
                if 'Knight' in new_zd[i][-1]:
                    #说话人为真
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                if int(zzb[wz]) == 1:
                                    if zzb.count('1') >= 1:
                                        temp_t_f.append(zzb)
                                    #说话人为假
                                else:
                                    if zzb.count('1') == 0:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    #说话人为真
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                if int(zzb[wz]) == 1:
                                    if zzb.count('0') >= 1:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f
                        #说话人为假的情况不存在

            elif 'least one of' in k or ' or ' in k:
                # if i in new_zd[i]:  # 判断说话涉及到的人是否包含说话的人(不需要判断说话的人不在这个里面）
                if 'Knight' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y >= 1:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y == 0:
                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y <= n - 1:
                                temp_t_f.append(zzb)
                        # 说话人为假不存在这种情况
                    t_or_f = temp_t_f

            elif 'most one of us' in k:
                if 'Knight' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                # 说话人为真
                                if int(zzb[wz]) == 1:
                                    if zzb.count('1') == 1:
                                        temp_t_f.append(zzb)
                                # 说话人为假
                                if int(zzb[wz]) == 0:
                                    if zzb.count('1') >= 2:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                # 说话人为真
                                if int(zzb[wz]) == 1:
                                    if zzb.count('0') <= 1:
                                        temp_t_f.append(zzb)
                                # 说话人为假
                                if int(zzb[wz]) == 0:
                                    if zzb.count('0') >= 2:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

            elif 'most one of' in k:
                # if i in new_zd[i]:  # 判断说话涉及到的人是否包含说话的人
                if 'Knight' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y <= 1:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y >= 2:
                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y >= len(new_zd[i]) - 2:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y <= n - 2:
                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

            elif 'xactly one of us' in k:
                if 'Knight' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                # 说话人为真
                                if int(zzb[wz]) == 1:
                                    if zzb.count('1') == 1:
                                        temp_t_f.append(zzb)
                                # 说话人为假
                                if int(zzb[wz]) == 0:
                                    if zzb.count('1') != 1:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                # 说话人为真
                                if int(zzb[wz]) == 1:
                                    if zzb.count('0') == 1:
                                        temp_t_f.append(zzb)
                                # 说话人为假
                                if int(zzb[wz]) == 0:
                                    if zzb.count('0') != 1:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

            elif 'xactly one of' in k:
                # if i in new_zd[i]:  # 判断说话涉及到的人是否包含说话的人
                if 'Knight' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y == 1:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y != 1:
                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y == n - 1:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y != n - 1:
                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

            elif 'll of us' in k:
                if 'Knight' in new_zd[i][-1]:
                    #说话人为真
                    for zzb in t_or_f:
                        if zzb.count('1') == len(zzb):
                            temp_t_f.append(zzb)
                    #说话人为假 说明意思为至少有一个人是假的
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                if int(zzb[wz]) == 0:
                                    temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    #speaker is 假 说明意思为至少一个人为真
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            for zzb in t_or_f:
                                if int(zzb[wz]) == 0:
                                    if zzb.count('1') >= 1:
                                        temp_t_f.append(zzb)
                    t_or_f = temp_t_f

            elif 'I am' in k:
                if 'Knight' in new_zd[i][-1]:
                    pass

                if 'Knave' in new_zd[i][-1]:
                    t_or_f = []

            elif ' are ' in k and ' and ' in k:
                # if i in new_zd[i]:  # 判断说话涉及到的人是否包含说话的人
                if 'Knight' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真
                        if int(zzb[speaker_wz]) == 1:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y == n:
                                temp_t_f.append(zzb)
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            temp_t_f.append(zzb)

                if 'Knave' in new_zd[i][-1]:
                    speaker_wz = sirs_names.index(i)
                    for zzb in t_or_f:
                        # 说话人为真不存在
                        # 说话人为假
                        if int(zzb[speaker_wz]) == 0:
                            n = 0
                            y = 0
                            while n < len(new_zd[i]) - 1:
                                y = y + int(zzb[sirs_names.index(new_zd[i][n])])
                                n += 1
                            if y >= 1:
                                temp_t_f.append(zzb)
                t_or_f = temp_t_f

            elif ' is ' in k:
                if 'Knight' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            speaker_wz = wz
                            for po in range(len(sirs_names)):
                                if sirs_names[po] == new_zd[i][0]:
                                    role_wz = po
                                    for zzb in t_or_f:
                                        #说话人为真
                                        if int(zzb[speaker_wz]) == 1:
                                            if int(zzb[role_wz]) == 1:
                                                temp_t_f.append(zzb)
                                        #说话人为假
                                        if int(zzb[speaker_wz]) == 0:
                                            if int(zzb[role_wz]) == 0:
                                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

                if 'Knave' in new_zd[i][-1]:
                    for wz in range(len(sirs_names)):
                        if sirs_names[wz] == i:
                            speaker_wz = wz
                            for po in range(len(sirs_names)):
                                if sirs_names[po] == new_zd[i][0]:
                                    role_wz = po
                                    for zzb in t_or_f:
                                        #说话人为真
                                        if int(zzb[speaker_wz]) == 1:
                                            if int(zzb[role_wz]) == 0:
                                                temp_t_f.append(zzb)
                                        #说话人为假
                                        if int(zzb[speaker_wz]) == 0:
                                            if int(zzb[role_wz]) == 1:
                                                temp_t_f.append(zzb)
                    t_or_f = temp_t_f

    # print(t_or_f)
    # print('分界线')
    return t_or_f

def standard_result(sirs_names, result):
    print('The Sirs are: ',end='')
    for i in range(len(sirs_names) - 1):
        print(sirs_names[i],end=' ')
    print(sirs_names[-1])
    if len(result) == 0:
        print('There is no solution.')
    if len(result) == 1:
        l = list(result[0])
        print('There is a unique solution:')
        for i in range(len(sirs_names)):
            if int(l[i]) == 1:
                print(f'Sir {sirs_names[i]} is a Knight.')
            if int(l[i]) == 0:
                print(f'Sir {sirs_names[i]} is a Knave.')
    if len(result) > 1:
        print(f'There are {len(result)} solutions.')

if __name__ =='__main__':
    try:
        file_name = input("Which text file do you want to use for the puzzle? ")
        with open(file_name)as file_object:
            text = file_object.read()
            sirs_names1 = find_names(text)
            old_zd = create_zd(text, sirs_names1)
            result = decide(sirs_names1, old_zd)
            standard_result(sirs_names1, result)
    except FileNotFoundError:
        print('Sorry, there is no such file.')
        sys.exit()















