#!/usr/bin/env python3
# *-* coding: utf-8 *-*
#@Time: 2019/05/15
#@Author: witchess
#@File: multiplication_table.py
#@Contact: 1822980791@qq.com


print("\n".join("\t".join(["%s * %s = %s" % (x, y ,x*y) for y in range(1,x+1)]) for x in range(1,10)))