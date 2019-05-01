python.md
# python final exam:


# 1. prime judgement:
from math inport sqrt
def prime(n):
	if n<= 1:
		return 0
	for i in range(2,int(sqrt(n)+1)):
		if n % i == 0:
			return 0
	return 1

# 1.2 prime judgement

def is_prime(n):
	return all(n % d for d in range(3, round(sqrt(n)) + 1, 2)) # ??????

# 1.3. find all prime num that less than N
prime_list = []
l = list(range(2,N))
for i in l:
	if prime(i):
		prime_list.append(i)
print(prime_list)

# 1.3 斐波那契数列

def fb(n):
	p = 1
	c = 1
	number = []
	while c <= n:
		p, c = c, p+c
	return number
# 1,3,1 斐波那契数列第n位
def fb2(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fb2(n-1) + fb2(n-2)
# 1.4 去除相邻重复字符
def rm_r(word):

	res = word[0]
	for i i word:

# according special formate to printing some pattern(triangle)

for n in range(N + 1):
    print(' ' * width * (N - n), end = '') # 确定没行前面需要打印的空格个数
    print((' ' * width).join((f'{pascal_triangle[n][k]:{width}d}' for k in range(n + 1)))) # 打印


 print('{} + 2 = {}'.format(n,n-1)) #格式输出

 # 除数余数计算
 m,a = divmod(m,10)



 # 很省事的包
 from math import sqrt
from collections import Counter,defaultdict,deque
# d = defaultdict(list)
import numpy as np
from itertools import compress,combinations,permutations,chain,groupby,zip_longest
 >>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

from math import sqrt
from collections import Counter,defaultdict,deque
import numpy as np
from itertools import compress,combinations,permutations,chain,groupby,zip_longest

compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
chain('ABC', 'DEF') --> A B C D E F
accumulate([1,2,3,4,5]) --> 1 3 6 10 15
zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
permutations()  p[, r]  长度r元组，所有可能的排列，无重复元素
permutations('ABCD', 2)     AB AC AD BA BC BD CA CB CD DA DB DC
combinations()  p, r    长度r元组，有序，无重复元素
combinations('ABCD', 2)     AB AC AD BC BD CD
product('ABCD', repeat=2)       AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
combinations_with_replacement() p, r    长度r元组，有序，元素可重复
combinations_with_replacement('ABCD', 2)        AA AB AC AD BB BC BD CC CD DD




