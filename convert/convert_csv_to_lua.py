#! /usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import const_data
import generater.lua as lua_gen
import sys
import os
import os.path


def csv_file_to_lua(csv_file,lua_file):
	
	def create_csv_reader(csv_file):
		return csv.reader(file(csv_file, 'rb'))
	
	def on_lua_gen_suc(luastr,data_name):
		print 'convert ',data_name,'succ'
		with open(lua_file,'wb') as tmp:
			tmp.write(luastr)
	const_data.convert(csv_file,create_csv_reader,lua_gen.create_gen(on_lua_gen_suc))


def convert_dirs(csv_dir,out_dir):
	for root,dirs,files in os.walk(csv_dir):
		for filepath in files:
			tablePath = os.path.join(root,filepath)
			csv_file_name = os.path.split(tablePath)[1];
			filess = csv_file_name.split('.');
			if filess == None or len(filess) <2 or filess[1] != 'csv' or  filess[0].find('~$') != -1:
				print 'ignore file', tablePath
				continue
			file_name = filess[0];
			print ' open file', tablePath
			csv_file_to_lua(tablePath,os.path.join(out_dir,file_name + '.lua'))

csv_file = None
csv_dir = None
out_dir = None
argn = len(sys.argv)
for x in range(0,argn):
	if x + 1 < argn:
		arg = sys.argv[x+1]
		if sys.argv[x] == '-csv':
			csv_file = arg
		if sys.argv[x] == '-dir':
			csv_dir = arg
		if sys.argv[x] == '-out_dir':
			out_dir = arg

src_dir = os.path.dirname( os.path.realpath(__file__) )
if csv_file != None:
	csv_file = os.path.join(src_dir,sys.argv[2])
	if out_dir == None:
		out_dir = os.path.dirname(os.path.realpath(csv_file))
	lua_file = os.path.join(out_dir,os.path.basename(csv_file).split('.')[0]) + '.lua'
	csv_file_to_lua(csv_file,lua_file)
elif csv_dir != None:
	if out_dir == None:
		out_dir = os.path.dirname(os.path.realpath(csv_dir))
	convert_dirs(csv_dir,out_dir)
else:
	print 'usage:  python ./convert_csv_to_lua.py -cvs csv_file -out_dir lua_dir\n\tpython ./convert_csv_to_lua.py -dir csv_dir -out_dir lua_dir'

