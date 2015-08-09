
import json

def file_ext():
	return '.json'
def create_gen(callback):
	def gen(data_dic,data_name):
		callback(json.dumps(data_dic,indent=2),data_name)
	return gen