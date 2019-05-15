#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Time: 2019/05/15
#@Author: witchess
#@File: copy.py
#@Contact: 1822980791@qq.com


import copy


def do_assign():
	"赋值"
	list1 = [1, 2, 3, ['a','b']]
	b = list1
	print(b) 


def do_copy():
	"浅拷贝：只拷贝父对象，不拷贝对象内部的子对象，改变内部子对象，拷贝对象和被拷贝对象都改变"
	list2 = [1, 2, 3, ['a','b']]
	c = list2.copy()
	print(c)
	list2.append(5)
	print(c,list2)  #拷贝对象此时不变
	list2[3].append('c')
	print(c,list2)  #子对象被改变，此时拷贝对象和被拷贝对象都改变


def do_deepcopy():
	"深拷贝：父子对象都拷贝，改变内部子对象，拷贝对象和被拷贝对象都改变"
	list3 = [1, 2, 3, ['a','b']]
	d = copy.deepcopy(list3)
	print(d)
	list3.append(5)
	print(d,list3)  #拷贝对象不变
	list3[3].append('c')
	print(d,list3)  #拷贝对象不变


if __name__ == '__main__':
    do_assign()
    do_copy()
    do_deepcopy()
