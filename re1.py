#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Time: 2019/05/14
#@Author: witchess
#@File: re1.py
#@Contact: 1822980791@qq.com

import re


def checkMail(str):
	"""
	匹配邮箱
	"""
	pattern = r'\w[0-9a-zA-Z]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
	res = re.findall(pattern,str)
	return res


if __name__ == '__main__':
	text = input("Please input a string:")
	fn1 = checkMail(text)
	print(fn1)