#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Desc(object):
	def __init__(self, default):
		self.data = default
	def __get__(self, instance, cls):
		print instance, cls, "GET"
		return self.data

	"""
	此处是instance，实际用class访问描述符，的确不会调到该函数
	"""
	def __set__(self, instance, value):
		print instance, "SET"
		self.data = value

class Data(object):
	desc = Desc(0)

data = Data()
print Data.desc, "\n", data.desc
data.desc = 1000
print Data.desc, "\n", data.desc
Data.desc = 9999
print Data.desc, "\n", data.desc
"""Output
None <class '__main__.Data'> GET
0
<__main__.Data object at 0x102997a50> <class '__main__.Data'> GET
0
<__main__.Data object at 0x102997a50> SET
None <class '__main__.Data'> GET
1000
<__main__.Data object at 0x102997a50> <class '__main__.Data'> GET
1000
9999
9999
说明：最后Data.desc = 9999,因为使用类设置的，所以没有走入描述符的__set__，然后desc的类型就不是Desc，
最后的print Data.desc, "\n", data.desc也就不会走入Desc的描述符__get__流程。
"""

