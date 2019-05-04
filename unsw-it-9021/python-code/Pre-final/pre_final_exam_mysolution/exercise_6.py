# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def rectangle(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> rectangle(1, 1)
    a
    >>> rectangle(2, 3)
    ab
    dc
    ef
    >>> rectangle(3, 2)
    abc
    fed
    >>> rectangle(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
#    q = ord('a')
#    for i in range(height):
##        print((i//width)%2)
#        if i%2 ==0:
#            for j in range(1,width+1):
#                if i <= j*width:
#                    if  q+j-1 < ord('a')+26:
#                        p = q+j-1
#                    else:
#                        q-=26
#                        p =q+j-1
#                    print(chr(p),end='')
#        else:
#            for j in range(1,width+1):
#                if i<=j*width:
#                    if (q-j+width) < ord('a')+26:
##                        p = q-j +width
#                        pass
#                    elif q-j+width < ord('a'):
#                        q += 26
#                    else:
#                        q -= (width)
#                    p= (q-j+width)
#                    print(chr(p),end='')
#        q += j
#        print()
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE
    res = []
    for i in range(height):
        res.append([])
        a =res[i]
        if i % 2 ==0:
            start = i*width
            for j in range(width):
                if start+j < 26:
                    pass
                elif start+j >= 26:
                    start = (start+j)%26 -j
                res[i].append(chr(ord('a')+start +j))
        else:
            start = (i+1) * width -1
            for j in range(width):
                if start-j < 0:
                    start = start+26
                elif start -j >26:
                    start = start%26
                res[i].append(chr(ord('a')+start-j))
    for i in range(len(res)):
        print(''.join(res[i]))

#rectangle(10,20)
if __name__ == '__main__':
    import doctest
    doctest.testmod()
