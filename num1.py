#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/10
#@Author: witchess
#@File: num1.py
#@Contact: 1822980791@qq.com

def no_repat():
    m = 0
    for i in range(1,6):
    	for j in range(1,6):
    		for k in range(1,6):
    			if (i != j) and (i != k) and (j != k):
    				m += 1
    				print("{}{}{}\t".format(i,j,k),end='|')
    print('m=',m)


def main():
	no_repat()


if __name__ == '__main__':
    main()