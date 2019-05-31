#!/usr/bin/env python3
#*-* coding: utf-8 *-*
#@Time: 2091/05/31
#@Author: witchess
#@File: prime.py
#@Contact: 1822908791@qq.com


def is_prime(x):
	if x < 2 :
		return False
	for i in range(2,x):
		if x % i == 0:
			return False
	return True


for x in filter(is_prime, range(20,30)):
	print(x)
