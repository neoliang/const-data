import csv
import json
import os
import shutil
import string
import sys
import json
import types

def get_data_desc(data_reader):
	dic = []
	dump_var = 0
	columnNames = []
	columnTypes = []
	while 1:
		try:
			row = data_reader.next()
			if data_reader.line_num == 2:
				columnNames = row
			elif data_reader.line_num == 3:
				columnTypes = row
			elif data_reader.line_num > 3:
				break
		except StopIteration:
			break
	for i, name_type in enumerate(zip(columnNames, columnTypes)):
		fname, ftype = name_type
		var_name = fname
		var_type = ftype
		var_type_name = ftype
		var_extra = None
		if var_name == '':
				print 'data desc error'
				continue
		var_def = {}
		var_def['seq_num'] = i
		var_def['type'] = var_type or 'int32'
		var_def['name'] = var_type_name or 'int32'
		var_def['var_name'] = var_name;
		if var_extra != None:
			var_def['extra'] = var_extra
		dic.append(var_def)
	return dic

def convert_json_to_table(data):
	data_dic = None
	try:
		data_dic = json.loads(data)
	except Exception, e:
		data_dic =[]
	return data_dic

def get_data_dic_for_row(row,dataDesc):

	data_dic = {}
	for i, data_row_and_desc in enumerate(zip(row, dataDesc)):
		data, data_desc = data_row_and_desc

		if data_desc['type'] == 'string':
			data = str(data)
		elif data_desc['type'] == 'json':
			data = convert_json_to_table(data)
		elif data_desc['type'] == 'bool':
			if data == '0' or data == '' or data == 'false' or data == 'False':
				data = False
			else:
				data = True
		elif data_desc['type'] == 'float':
			if data == '':
				data = 0
			data = float(data)
		elif data_desc['type'] == 'comment':
			continue
		else:
			if data == '':
				data = 0
			data = int(data)

		data_dic[data_desc['var_name']] = data
	return data_dic

def get_datas(data_reader,dataDesc,dbName):
	data_list = []
	while True:
		try:
			row = data_reader.next()
			if data_reader.line_num <= 3:
				continue
			rowdesc = get_data_dic_for_row(row,dataDesc)
			data_list.append(rowdesc)
		except StopIteration:
			break
	return data_list

def convert(filePath,fileReader,generate):
	file_name = None
	data_desc = None
	try:
		data_file_name = os.path.split(filePath)[1];
		file_name = data_file_name.split('.')[0];
		data_desc = get_data_desc(fileReader(filePath))
	except Exception, e:
		print 'convert ',filePath ,'failed'
		raise
	
	data_list = get_datas(fileReader(filePath),data_desc,file_name)
	generate(data_list,file_name)
