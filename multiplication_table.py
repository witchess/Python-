#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/15
#@Author: witchess
#@File: multiplication_table.py
#@Contact: 1822980791@qq.com


def fun1():
	"""一行代码实现乘法表"""
	print("\n".join("\t".join(["{}*{} = {:2}".format(x, y, x*y) for y in range(1,x+1)])for x in range(1,10)))
    

def fun2():
	"""乘法表的常规表示---左上三角"""
	for i in range(1,10):
		for j in range(1,i+1):
			print('%d*%d = %2s\t' % (j,i,i*j), end='')
		print()


def fun3():
	"""长方形完整格式"""
	for i in range(1,10):
		for j in range(1,10):
			print("{}*{} = {:2}\t".format(i, j, i*j), end='')
		print("")


def fun4():
	"""左上三角格式"""
	for i in range(1,10):
		for j in range(i,10):
			print("{}*{} = {:2}\t".format(i, j, i*j), end ='')
		print("")


def fun5():
	"""右上三角格式"""
	for i in range(1,10):
		for k in range(1,i):
			print(end="         ")
		for j in range(i,10):
			print("{}*{} = {:2}".format(i, j, i*j), end =' ')
		print("")


def fun6():
	"""右上三角格式"""
	for i in range(1,10):
		for k in range(i,10):
			print(end="         ")
		for j in range(1,i):
			print("{}*{} = {:2}".format(i, j, i*j),end=' ')
		print("")


def main():
	f1 = fun1()
	f2 = fun2()
	f3 = fun3()
	f4 = fun4()
	f5 = fun5()
	f6 = fun6()


if __name__ == '__main__':
	main()



