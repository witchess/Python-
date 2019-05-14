#!/usr/bin/env python3
#-*- coding utf-8 -*-

"""返回列表中出现次数最多的元素"""
from collections import Counter


def max_list(lt):
	temp = 0 
	for i in lt:
		if lt.count(i) > temp:
			max_str = i
			temp = lt.count(i)
	return max_str



if __name__ == '__main__':
	fn1 = max_list(["mary","mary","mary",1,1,2])
	print(fn1)#mary