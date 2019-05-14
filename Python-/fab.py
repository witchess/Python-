#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
斐波那契数
"""

#用函数来求解
def Fab_function(max):
	s, a, b = 0, 0, 1
	L = []
	while s < max:
		L.append(b)
		a, b = b, b+a 
		s += 1
	return L 


#用生成器yield来求解
def Fab_yield(max):
	s ,a ,b = 0, 0, 1
	while s < max:
		yield b 
		a, b = b, a+b
		s += 1


if __name__ == '__main__':
	fn1 = Fab_function(10)
	print(fn1)
	fn2 = Fab_yield(10)
	for i in fn2:
		print(i)