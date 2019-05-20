#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/20
#@Author: witchess
#@File: decorator.py
#@Contact: 1822980791@qq.com


def make_decorator(func):
	'''无参数'''
	def wrapped(*args, **kwargs):
		ret = func(*args, **kwargs)
		return '<i>' + ret + '</i>'
	return wrapped

@make_decorator
def hello(name):
	return "hello %s" % name 
print(hello("Python"))



def wrap_in_tag(tag):
	def decorator(fun):
		def wrapped(*args, **kwargs):
			ret = fun(*args, **kwargs)
			return '<' + tag + '>' + ret + '</' + tag + '>'
		return wrapped
	return decorator
make_decorator1 = wrap_in_tag('b')

@make_decorator1
def hello(name):
	return "hello %s " % name

print(hello("python3"))