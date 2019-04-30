'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    d = {}
    with open('cpiai.csv') as f:
        content_lines = f.readlines()
    for l in content_lines:
        if str(year) in l:
            dat, inde, inf = l.split(',')
            y,m,da = dat.split('-')
            inf = inf[:-1]
            d[m] = float(inf.strip())
    k = max(d.values())
    m_list = []
    for i in d.keys():
        if d[i] == k:
            m_list.append(months[int(i)-1])
    print(f'In {year}, maximum inflation was: {k}')
    print('It was achieved in the following months: ',end='')
    print(', '.join(m_list))
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()
