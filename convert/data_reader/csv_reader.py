import csv

def create_data_tables(csv_file):
	csvReader = csv.reader(file(csv_file, 'rb'))
	data_tables = []
	while True:
		try:
			row = csvReader.next()
			data_tables.append(row)
		except StopIteration:
			break
	return data_tables