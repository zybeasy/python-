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
