import xlrd

def file_ext():
	return 'xlsx'
def create_data_tables(excel_file):
	data_tables = []
	workbook = xlrd.open_workbook(excel_file)
	booksheet = workbook.sheets()[0]
	for row in xrange(booksheet.nrows):
		row_data = []
		for col in xrange(booksheet.ncols):
			row_data.append(booksheet.cell(row, col).value)
		data_tables.append(row_data)
	return data_tables