#!/usr/bin/env python3
#*-* coding: utf-8 *-*
#@Time: 2091/05/31
#@Author: witchess
#@File: filter1.py
#@Contact: 1822908791@qq.com

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False


for x in filter(is_even, range(1,20)):
	print(x)
