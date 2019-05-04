# You might find the ord() function useful.
from itertools import groupby

def longest_leftmost_sequence_of_consecutive_letters(word):
    '''
    You can assume that "word" is a string of
    nothing but lowercase letters.
    
    >>> longest_leftmost_sequence_of_consecutive_letters('')
    ''
    >>> longest_leftmost_sequence_of_consecutive_letters('a')
    'a'
    >>> longest_leftmost_sequence_of_consecutive_letters('zuba')
    'z'
    >>> longest_leftmost_sequence_of_consecutive_letters('ab')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('bcab')
    'bc'
    >>> longest_leftmost_sequence_of_consecutive_letters('aabbccddee')
    'ab'
    >>> longest_leftmost_sequence_of_consecutive_letters('aefbxyzcrsdt')
    'xyz'
    >>> longest_leftmost_sequence_of_consecutive_letters('efghuvwijlrstuvabcde')
    'rstuv'
    '''
    if not word:
        return ''
    st = word
#    for k,g in groupby(word):
#        st += k
    res = ''
    for i in range(len(st)):
        ss = st[i]
        for j in range(i+1,len(st)):
            if ord(st[j]) == ord(ss[-1])+1:
                ss += st[j]
            else:
                if len(ss) > len(res):
                    res = ss
                break
        if len(ss) > len(res):
            res = ss
    return res
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE                

#print(longest_leftmost_sequence_of_consecutive_letters('aabbddeeff'))
if __name__ == '__main__':
    import doctest
    doctest.testmod()
