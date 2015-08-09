import csv

def create_reader(csv_file):
	return csv.reader(file(csv_file, 'rb'))