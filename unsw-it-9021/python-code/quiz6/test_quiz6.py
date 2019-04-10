#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-10 10:23
# @Author  : ZD Liu

'''
>>> print(os.popen('echo 0 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 0 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 0 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 0
    0 1 0 0 1 0 1 0 0 1
    1 0 1 1 1 0 1 1 1 0
    0 0 1 0 1 1 0 1 0 0
    0 0 0 1 0 0 1 1 0 1
    1 0 1 0 1 1 0 1 1 0
    1 0 0 0 0 1 1 0 0 0
    0 0 0 1 1 0 0 1 1 1
    1 1 0 1 0 1 1 0 0 0
    1 0 0 1 0 1 1 0 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 0 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 0 1 0 1 0 0 1 1 1
    1 1 0 1 0 1 0 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 0 1 0 0 1 1 1
    1 1 0 1 1 1 0 1 1 1
    0 0 1 0 0 0 1 1 0 0
    1 1 1 0 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 0 1 0 0 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 0 0 1
    1 0 1 1 1 1 1 1 1 0
    0 0 1 0 1 1 1 1 0 1
    1 1 1 1 0 0 1 1 0 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 0 0 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 0
    1 0 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 0 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 0 0 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 0 0 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 0 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 0 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 0 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 0 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 0 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 0 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 0 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 1 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 1 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 0 1 1 1 1 0 0
    1 0 1 1 0 1 1 0 0 1
    0 0 0 0 1 0 1 0 0 1
    1 0 1 0 0 1 1 0 1 0
    0 1 0 1 1 0 1 1 1 1
    0 1 0 1 1 0 1 1 0 1
    0 0 1 1 1 0 1 0 1 1
    0 0 0 0 0 0 1 1 1 1
    1 0 1 0 0 1 0 1 1 0
    1 1 1 1 1 0 1 1 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 1 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 0 1 1 1 1 1
    0 0 1 0 1 1 1 0 1 1
    1 1 0 1 0 1 0 0 0 1
    1 0 1 1 0 1 1 0 1 0
    1 1 1 0 1 0 1 0 1 1
    0 1 1 1 0 0 1 1 1 0
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 0 1 1 1 1 1 1
    0 1 1 1 0 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 1 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 1 1 1 1 1 0
    1 0 1 1 0 1 1 1 0 1
    0 0 0 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 0
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 1 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 1
    0 1 0 1 1 1 0 1 1 1
    1 0 1 0 0 0 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 1 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 1 1 1 1 1
    1 0 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 0 0 0 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 1 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 0 0 0 1 1
    0 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 1 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    0 0 0 0 1 1 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 1 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    0 0 0 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 1 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 0 0 0 1 0 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 2 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 1 1 0 0 0
    1 1 1 1 1 0 0 1 1 1
    1 1 0 0 0 0 0 0 1 0
    0 1 0 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 0 1 1 0 1 0 0 0 0
    0 1 0 0 0 1 0 0 0 1
    0 0 1 1 0 0 0 0 0 0
    0 0 0 1 1 0 0 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 2 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 0 1 1 1 1 1
    0 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 0 1 0 0 0 0
    0 1 0 0 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 2 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 1 0 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 0 0
    0 1 1 0 1 1 1 1 0 1
    0 0 1 1 1 1 0 0 0 0
    0 0 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 0 1 0 0 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    0 1 1 1 1 1 1 1 0 1
    0 0 1 1 1 1 0 1 1 1
    0 0 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 0
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 3 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 3 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 1 1 0 0 1 1 0 0
    1 1 1 0 0 0 1 0 0 0
    0 1 0 1 1 1 1 1 1 0
    1 0 0 0 1 0 1 1 1 1
    1 1 1 0 1 0 1 0 1 0
    0 1 1 0 0 1 1 0 1 0
    1 0 0 1 1 1 0 0 0 1
    1 1 0 0 1 0 0 0 0 0
    1 1 1 0 0 1 1 1 0 1
    1 1 1 0 1 1 0 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 3 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 1 1 1 1 1 0
    1 0 1 1 1 0 0 1 1 1
    1 1 1 1 0 0 1 0 1 1
    1 0 1 0 0 1 0 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 0 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 0
    1 1 1 1 1 0 1 1 0 1
    1 1 1 0 0 1 1 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 3 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
    0 1 0 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 0 0 1 1 0 1 0
    1 1 0 1 1 1 0 0 0 1
    1 1 1 0 1 0 0 0 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 3 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 0 0 1 1 0
    1 0 1 1 0 1 1 1 0 0
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 3 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 0 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 0 1 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 3 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 3 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 0 1
    1 1 1 0 1 0 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 3 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 0 1 1 1
    1 1 1 0 1 0 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 3 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 4 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 4 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 0 0 0 0 1
    1 0 0 1 1 0 0 1 0 0
    1 1 0 0 1 1 1 0 1 1
    0 0 0 1 1 0 1 0 1 1
    0 1 1 1 1 1 0 0 1 1
    0 0 0 1 1 1 1 0 0 0
    1 0 1 1 0 1 1 1 0 1
    0 0 0 1 0 0 1 0 1 1
    0 0 1 0 1 1 0 1 1 1
    0 1 0 1 0 1 1 0 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 4 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 0 1 1 1 0 0 0 0
    1 1 1 0 0 1 1 1 1 0
    0 1 0 0 1 1 1 0 0 1
    1 1 1 1 0 1 1 1 1 1
    0 0 0 1 1 0 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    1 0 0 1 1 0 0 0 1 1
    1 1 1 1 1 1 1 0 1 0
    0 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 4 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 0 0 1
    1 0 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 0 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 0 1 1 1 1
    0 0 1 0 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 4 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 0 0 0 1
    1 1 0 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    0 0 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
    0 1 1 1 1 0 0 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 4 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 0 0 0
    1 1 1 0 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 4 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 1 1 0 0 0
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 0 0 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 4 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 4 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 4 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 5 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 5 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 0 0 0 0 1 1
    0 1 0 0 0 0 1 1 0 1
    0 0 0 1 0 0 0 0 0 0
    0 0 1 1 0 0 0 0 1 1
    0 1 1 0 0 1 0 1 1 0
    1 0 1 1 1 1 1 0 1 1
    0 0 1 0 1 1 0 1 1 1
    0 1 0 0 0 0 0 1 1 1
    1 1 0 1 1 0 1 0 0 1
    1 0 1 1 0 1 1 1 0 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 5 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    0 1 0 0 0 1 1 0 1 1
    0 1 0 0 1 0 1 1 0 1
    0 0 0 1 1 1 0 0 0 0
    0 0 0 0 1 1 0 1 1 1
    0 0 1 0 1 1 0 1 1 0
    0 1 0 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 0
    1 1 1 0 0 1 0 1 1 1
    0 1 1 1 1 1 0 1 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 5 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 0 1 0 1 1
    1 1 0 1 0 1 1 1 1 1
    1 0 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 1 0
    1 0 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 0 1 1 1
    0 1 0 1 1 0 1 1 1 1
    1 1 0 1 1 0 1 0 1 1
    1 1 1 1 0 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 5 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 0 1 0
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 0 1 1 1
    1 1 0 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 5 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 0 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 1
    0 1 1 1 1 1 0 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 5 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 5 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 5 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 1 0
    1 1 1 1 0 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 5 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 1 0 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 6 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 6 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 0 0 1 1 1 0
    1 1 0 1 0 0 1 0 1 1
    0 1 1 1 1 0 0 1 0 0
    0 1 1 0 0 1 0 1 1 1
    0 0 0 0 1 1 0 1 1 0
    0 0 0 0 0 0 1 1 1 1
    1 1 0 1 0 0 1 1 0 1
    0 0 1 1 1 0 1 1 1 1
    0 0 1 1 1 0 0 0 0 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 6 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 0 0 1 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 0 0 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 0 0 1 1 1 0 0 1 0
    1 1 1 0 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 0 0
    1 1 1 0 0 1 1 1 1 1
    0 1 1 0 0 1 0 1 1 0
    0 0 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 6 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 0 1 1 1 1 0
    1 1 1 1 0 1 1 0 1 1
    0 1 1 1 1 0 1 1 0 0
    1 1 1 1 0 1 1 1 1 1
    0 0 1 0 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 0 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 0 0 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 6 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 0 1 1 1 1
    1 0 1 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 1
    1 1 0 1 1 0 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 0 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 6 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 0 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 0 0
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 6 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 0 0 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 6 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 0 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 6 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 6 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 7 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 0 0 0 1 0 0 0
    0 1 1 0 0 0 1 0 0 0
    0 1 0 0 0 0 1 1 0 0
    1 0 0 0 1 0 0 0 0 1
    1 1 1 1 1 1 0 0 0 0
    1 1 1 1 1 0 0 1 0 1
    0 1 1 0 0 1 1 1 1 1
    0 0 1 1 0 0 1 1 1 1
    1 0 1 1 0 0 1 0 0 1
    0 0 1 1 1 0 0 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 7 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 0 1 0 1 1
    0 1 0 0 0 1 1 0 0 0
    1 1 0 1 0 0 1 1 1 0
    1 1 1 0 0 0 1 0 1 1
    0 1 0 1 1 1 1 0 0 1
    1 1 0 1 0 1 1 0 1 0
    1 0 1 1 1 1 1 1 1 1
    1 1 0 0 1 0 0 1 1 1
    1 1 1 1 1 1 0 0 1 1
    0 1 0 1 1 0 1 0 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 7 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 0 1 0 1 0
    0 1 1 0 1 0 1 0 0 1
    0 1 0 1 0 1 1 1 1 0
    1 1 0 1 1 0 0 0 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 0 1 1 1
    1 1 1 0 0 1 1 1 1 1
    0 0 1 1 0 0 1 1 1 1
    1 0 1 1 1 0 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 7 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 1 0 1 1 0
    1 1 0 0 1 1 0 1 0 1
    1 0 1 0 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 0
    1 1 1 1 0 1 1 1 1 0
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 0 0 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 7 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 0 1 1
    0 1 1 0 0 1 1 0 1 0
    1 1 0 1 0 1 1 1 1 0
    1 1 1 0 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 1 1 1 0 1 1 0 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 0 1 0 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 7 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 1 0 1
    1 0 1 1 0 0 1 1 0 1
    0 1 1 0 1 1 0 1 1 1
    1 0 1 1 1 0 1 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 0 1
    1 0 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 0 0 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 7 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 0 1 0
    1 1 1 1 1 1 1 0 1 1
    0 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 7 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 0 1
    1 0 1 1 1 1 1 1 1 1
    0 1 1 0 1 0 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 0 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    0 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 8 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 8 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 0 0 0 0 0 0
    1 0 1 1 1 1 1 0 1 0
    1 0 0 1 1 1 1 0 1 0
    0 1 1 0 0 1 0 0 1 0
    0 0 0 1 0 0 1 1 1 1
    1 0 0 0 1 1 1 0 1 0
    1 1 0 0 1 0 0 1 1 0
    1 0 1 1 1 1 1 0 1 0
    0 0 0 0 1 0 0 1 1 0
    1 0 0 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 8 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 1 1 0 0 1 0 0 0 0
    1 0 1 1 0 1 1 1 1 1
    1 0 1 0 1 0 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 1 0 1 0 1 0 1 0 1
    1 1 0 1 0 1 0 1 0 1
    1 0 0 1 1 1 1 1 1 1
    1 1 0 0 1 0 1 1 1 1
    1 1 1 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 0 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 8 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 0 1 1 1
    1 0 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 0 1 0
    0 1 1 0 0 1 1 0 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 0
    1 0 1 1 1 0 0 1 1 1
    1 1 1 1 1 1 1 0 0 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 8 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 0 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 0 1 1 0 1 1 1 1 1
    0 1 0 0 1 1 1 0 0 1
    1 0 1 1 1 1 1 1 0 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 8 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 0 1 1 0 1 1 1
    1 1 1 1 0 1 1 0 0 1
    1 1 0 1 0 1 1 1 0 1
    1 1 1 1 1 1 0 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 8 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 0 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    0 1 0 1 1 1 1 0 1 0
    1 1 1 0 1 1 1 1 1 1
    1 1 0 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 8 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 8 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 8 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 9 0 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0
The largest isosceles triangle has a size of 0
>>> print(os.popen('echo 9 1 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 0 0 0 1 1 0 1
    0 1 0 1 1 0 0 0 0 0
    0 0 1 0 1 0 0 1 0 1
    0 1 1 1 0 0 0 1 0 1
    1 0 0 0 1 0 0 0 0 0
    1 0 0 0 0 0 1 0 1 0
    1 0 0 0 0 0 0 1 0 1
    0 0 1 0 0 0 1 0 1 0
    1 1 0 1 0 0 1 1 0 1
    0 0 0 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 9 2 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 0 0 1 0 1 1
    1 1 0 1 1 1 1 0 1 1
    0 1 1 1 1 0 0 0 0 0
    0 1 1 0 1 1 1 0 1 0
    1 0 1 1 0 1 0 1 1 1
    0 0 1 0 1 0 1 1 0 0
    0 1 1 0 1 0 0 1 0 0
    1 0 0 0 1 0 1 0 1 1
    1 0 1 0 1 0 1 0 1 1
    0 0 1 1 0 0 1 1 1 1
The largest isosceles triangle has a size of 2
>>> print(os.popen('echo 9 3 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 0 1
    0 1 1 1 1 1 1 1 0 0
    1 0 1 0 1 1 1 1 0 1
    1 1 1 1 0 1 0 1 0 1
    1 1 0 1 1 0 0 0 1 1
    1 0 0 1 0 0 1 1 1 0
    1 1 0 1 1 0 0 1 1 1
    0 0 1 1 1 0 1 0 1 0
    1 1 1 1 1 0 1 1 0 1
    0 1 1 1 1 1 0 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 4 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 0 1 1 1 0 1 1 1 1
    1 1 1 0 0 1 1 1 0 1
    0 1 1 1 1 0 1 1 1 1
    1 0 1 0 1 0 1 1 1 0
    1 1 0 1 0 0 1 1 1 1
    0 0 1 1 0 1 0 1 1 1
    1 1 0 1 1 0 1 1 1 1
    0 0 1 1 1 1 1 1 0 0
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 5 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 0 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 0 0
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 0 1 0 1 1 1 0
    1 1 1 0 1 0 0 1 1 1
    1 0 0 1 1 0 1 0 1 1
    1 1 1 0 1 1 1 0 1 1
    1 1 1 1 0 0 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 6 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 0 1
    1 1 1 0 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 0
    0 1 1 1 1 0 1 1 1 1
    1 0 1 1 1 1 1 1 1 0
    1 1 1 1 1 1 1 0 1 1
    0 1 0 1 1 1 1 0 1 1
    1 1 0 1 0 0 1 1 1 1
    1 1 0 0 1 1 0 1 0 1
    1 1 1 1 0 1 1 1 1 0
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 7 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    0 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 0 1 0 1
    1 1 0 1 1 1 0 1 1 1
    1 0 1 1 0 1 1 1 1 1
    1 1 1 1 1 0 0 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 0 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 8 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 0 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 0
    1 0 1 1 1 0 1 1 1 0
    1 1 1 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 0 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
The largest isosceles triangle has a size of 3
>>> print(os.popen('echo 9 9 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 0 1 0 1 1 1 0
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 0 1 1 1 1 1 1 0 1
    1 1 1 1 1 0 1 1 1 1
The largest isosceles triangle has a size of 4
>>> print(os.popen('echo 0 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 1 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 2 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 3 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 4 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 5 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 6 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 7 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 8 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 9 100 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 14 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 15 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 0
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 16 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 0 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 17 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 0
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 40 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 49 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 50 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 88 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 14 99 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 14 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 0 1 1 1 0 0
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 0 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 15 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 0 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 0 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 16 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 0 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 17 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 0 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    0 1 1 1 1 0 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 0 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 40 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 0 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 49 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 50 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 0 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 88 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo 15 99 | python3 quiz_6.py').read(), end='')
Enter two integers: Here is the grid that has been generated:
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
    1 1 1 1 1 1 1 1 1 1
The largest isosceles triangle has a size of 5
>>> print(os.popen('echo a 99 | python3 quiz_6.py').read(), end='')
Enter two integers: Incorrect input, giving up.

>>> print(os.popen('echo 0 9a | python3 quiz_6.py').read(), end='')
Enter two integers: Incorrect input, giving up.

>>> print(os.popen('echo 10   | python3 quiz_6.py').read(), end='')
Enter two integers: Incorrect input, giving up.

'''


if __name__ == '__main__':
    import doctest
    import os
    print('Test Start......')
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
