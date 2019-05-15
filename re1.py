#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Time: 2019/05/14
#@Author: witchess
#@File: re1.py
#@Contact: 1822980791@qq.com

import re


def check_mail(str):
	"匹配邮箱"
	pattern = r'\w[0-9a-zA-Z]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$'
	res = re.findall(pattern,str)
	return res


def check_phone(strData):
	"匹配手机号码:第1位是1,第2位是[3,9],第3-11位是[0,9]"
	pattern = r'^1[3,9][0,9]{9}$'
	res = re.findall(pattern,strData)
	return res


def check_id(strData):
	"""匹配身份证号：第1位表示[1,6],第2-6位表示[0-9]{5}或\d{5},第7位表示[12]第8,9,10位表示\d{3}
	第11,12位表示：0[1-9]1[12]
	第13,14位表示：0[1-9]1[0-9]2[0-9]3[01]
	第15,16,17位表示：[0-9]或\d{3}
	第18位表示：[0-9]|x|X或\d|x|X
	"""
	pattern = r'^[1-6]\d{5}[12]\d{3}(0[1-9]|1[12])(0[1-9]|1[1-9]|2[0-9]|3[01])\d{3}(\d|x|X)$'
	res = re.findall(pattern,strData)
	return res


def check_web(str):
	"匹配网址"
	pattern = r'[a-zA-Z]+://[\S]*[.com|.net]'
	res = re.findall(pattern,str)
	return res


if __name__ == '__main__':
	text1 = input("Please input a mail: ")
	fn1 = check_mail(text1)
	print(fn1)
	text2 = input("Please input a phone number: ")
	fn2 = check_phone(text2)
	print(fn2)
	text3 = input("Please input your id: ")
	fn3 = check_id(text3)
	print(fn3)
	text4 = input("Please input: ")
	fn4 = check_web(text4)
	print(fn4)

