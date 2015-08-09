#! /usr/bin/env python
# -*- coding: utf-8 -*-
import const_data
import generater
import data_reader
import os
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def data_file_to_lua(csv_file,lua_file,reader,out_gen):
		
	def on_lua_gen_suc(luastr,data_name):
		print 'convert ',data_name,'succ'
		with open(lua_file,'wb') as tmp:
			tmp.write(luastr)
	const_data.convert(csv_file,reader,out_gen.create_gen(on_lua_gen_suc))


def convert_dirs(csv_dir,out_dir,reader,out_gen,file_ext):
	for root,dirs,files in os.walk(csv_dir):
		for filepath in files:
			tablePath = os.path.join(root,filepath)
			csv_file_name = os.path.split(tablePath)[1];
			filess = csv_file_name.split('.');
			if filess == None or len(filess) <2 or filess[1] != file_ext or  filess[0].find('~$') != -1:
				print 'ignore file', tablePath
				continue
			file_name = filess[0];
			print ' open file', tablePath
			data_file_to_lua(tablePath,os.path.join(out_dir,file_name + out_gen.file_ext()),reader,out_gen)
def print_help():
	print '''
	usage: python ./convert.py -if input_format -of output_format -file input_file -out_dir lua_dir
	python ./convert_csv_to_lua.py -if input_format -of output_format -dir csv_dir -out_dir lua_dir

	options:  
		-if: 	  input file format : csv or excel, current only support csv
		-of: 	  output file format lua,json
		-dir: 	  convert files in dir
		-file: 	  convert file
		-out_dir: the dir of output files
		-h print: this message 	
	'''
csv_file = None
csv_dir = None
out_dir = None
argn = len(sys.argv)
input_format = None
output_format = None
for x in range(0,argn):
	if sys.argv[x] == '-h':
		print_help()
		sys.exit()
	if x + 1 < argn:
		arg = sys.argv[x+1]
		if sys.argv[x] == '-file':
			csv_file = arg
		if sys.argv[x] == '-dir':
			csv_dir = arg
		if sys.argv[x] == '-out_dir':
			out_dir = arg
		if sys.argv[x] == '-if':
			input_format = arg
		if sys.argv[x] == '-of':
			output_format = arg

src_dir = os.path.dirname( os.path.realpath(__file__) )
try:
	reader = data_reader.reader[input_format].create_reader
	out_gen = generater.language[output_format]
	if csv_file != None:
		csv_file = os.path.join(src_dir,csv_file)
		if out_dir == None:
			out_dir = os.path.dirname(os.path.realpath(csv_file))
		lua_file = os.path.join(out_dir,os.path.basename(csv_file).split('.')[0]) + out_gen.file_ext()
		data_file_to_lua(csv_file,lua_file,reader,out_gen)
	elif csv_dir != None:
		if out_dir == None:
			out_dir = os.path.dirname(os.path.realpath(csv_dir))
		convert_dirs(csv_dir,out_dir,reader,out_gen,input_format)
	else:
		raise Exception("")
except Exception, e:
	print_help()
