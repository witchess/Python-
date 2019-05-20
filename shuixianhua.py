#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/20
#@Atthor: witchess
#@File: shuixianhua.py
#@Contact: 1822980791@qq.com

def shuixianhua_method1():
    '''高等函数'''
    result = list(map(lambda x: x[1], filter(lambda x: x[0], 
    	[(i**3 + j**3 + k**3 == i*100 + j*10 + k, i**3 + j**3 + k**3) for i in range(1,10) for j in range(0,10) 
    	for k in range(0,10)])))
    print(result)


def shuixianhua_method2():
	'''列表推导式'''
	result = [i**3 + j**3 + k**3 for i in range(1,10) for j in range(0,10) for k in range(0,10) 
	if i**3 + j**3 + k**3 == i*100 + j*10 +k]
	print(result)


if __name__ == '__main__':
	shuixianhua_method1()
	shuixianhua_method2()
