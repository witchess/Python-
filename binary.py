#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/20
#@Author: witchess
#@File: binary.py
#@Contact: 1822980791@qq.com


def binary_chop1(alist, data):
    """
    递归解二分查找
    :param alis
    :return
    """
    n = len(alist)
    mid = n // 2
    if len(alist) < 1:
        return False
    if alist[mid] > data:
        return binary_chop1(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop1(alist[mid+1,n],data)
    else:
    	return True


def binary_chop2(alist,data):
	n = len(alist)
	first = 0
	last = n-1
	while first <= last:
		mid = (first + last) // 2
		if alist[mid] > data:
			last = mid - 1
		elif alist[mid] < data:
			first = mid + 1
		else:
			return True


def main():
    if binary_chop1([1,2,3,4,5,6,7,8,9],5):
    	print("OK")
    if binary_chop2([1,2,3,4,5,6,7,8,9],4):
    	print("ok")


if __name__ == '__main__':
	main()