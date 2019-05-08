'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''


def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    res_dic = {}
    res_dic[1] = []
##    for k in letters:
##        res_dic[1].append(k)
##    for i in range(len(letter)-2):
##        for j in res_dic.keys:
##            res_dic[i+2] = []
##            for k in letters:
##                if k not in res_dic[j]:
##                    res_dic[i+2] = res_dic[j]+k
##    
##    for key in res_dic.keys():
##        for word in res_dic[key]:
##            all_posble.append(word)
##            all_posble.extend(get_list(word))

            
    with open(dictionary) as ff:
        words_list = ff.readlines()
    all_posble = {}
    f_list = max_letter(letters)
    for i in f_list:
        j =1
        while j < len(i):
            t1 = i[:j]
            t2 = i[j:]
            j += 1
            if t1 not in all_posble.keys():
                all_posble[t1] = t2
    for key in all_posble.keys():
        for word in max_letter(key):
            if word in words_list:
                for word2 in max_letter(all_posble[key]):
                    if word2 in words_list:
                        solutions.append((word,word2))
    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)
##def get_list(lis1):
##    res = []
##    for lis in [lis1]:
##        for i in range(len(lis)):
##            tem_lis = lis[i:] + lis[:i]
##            if isinstance(tem_lis,list) :
##                res.extend(tem_lis)
##            else:
##                res.append(tem_lis)
##    print(res)
##    return res
def max_letter(sss):
    res = []
    all = []
    res2 = []
    k = 0
    q = sss
    for i in sss:
        res.append(i)
    while k <= len(sss):
        res2 = []
        for j in res:
            for i in sss:
                if i not in j:
                    res2.append(i+j)
        res.extend(res2)
        k += 1
    for i in res:
        if len(i) ==len(sss) and i not in all:
            all.append(i)
    print(all)
    return all
##max_letter('AB')
##f('ABCD')
if __name__ == '__main__':
    f('AB')
