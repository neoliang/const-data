#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import types
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
def space_str(layer):
	spaces = ""
	for i in range(0,layer):
		spaces += '\t'
	return spaces

def dic_to_lua_str(data,layer=0):

	d_type = type(data)
	if  d_type is types.StringTypes or d_type is str or d_type is types.UnicodeType:
		yield ("'" + data + "'")
	elif d_type is types.BooleanType:
		if data:
			yield ('true')
		else:
			yield ('false')
	elif d_type is types.IntType or d_type is types.LongType or d_type is types.FloatType:
		yield (str(data))
	elif d_type is types.ListType:
		yield ("{\n")
		yield (space_str(layer+1))
		for i in range(0,len(data)):
			for sub in  dic_to_lua_str(data[i],layer+1):
				yield sub
			if i < len(data)-1:
				yield (',')
		yield ('\n')
		yield (space_str(layer))
		yield ('}')
	elif d_type is types.DictType:
		yield ("\n")
		yield (space_str(layer))
		yield ("{\n")
		data_len = len(data)
		data_count = 0
		for k,v in data.items():
			data_count += 1
			yield (space_str(layer+1))
			if type(k) is types.IntType:
				yield ('[' + str(k) + ']')
			else:
				yield (k) 
			yield (' = ')
			try:
				for sub in  dic_to_lua_str(v,layer +1):
					yield sub
				if data_count < data_len:
					yield (',\n')

			except Exception, e:
				print 'error in ',k,v
				raise
		yield ('\n')
		yield (space_str(layer))
		yield ('}')
	else:
		raise d_type , 'is error'
def file_ext():
	return 'lua'
def create_gen(callback):
	def gen(data_dic,data_name):
		luastr = ''
		for it in dic_to_lua_str(data_dic):
			luastr += it
		callback(luastr,data_name)
	return gen