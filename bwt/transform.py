'''
Module for performing forward Burrows-Wheeler transforms on strings
'''
def build_table(in_list):
	'''
	Returns a table (list) of strings where each element has character contents rotated by 1

		Parameters:
			in_list (list): of length 1, contains string to be transformed

		Returns:
			in_list (list): of lenght len(in_list), table of rotated in_list
	'''
	if len(in_list)<len(in_list[0]):
		in_list.append(in_list[-1][-1]+in_list[-1][0:-1])
		build_table(in_list)
	return in_list	

def sort_table(table):
	'''
	Lexically sorts a table (list)

		Parameters:
			table (list): a list of strings to be lexically sorted

		Returns:
			table (list): a lexically sorted list of strings
	'''
	table.sort()
	return table

def extract_last_column(table):
	'''
	Returns last column of table 

		Parameters:
			table (list): a list of strings

		Returns:
			last_columns (string): last characters of each element within table
	'''
	last_column = ''.join([table[i][-1] for i in range(len(table))]) 
	return last_column

def bwt(in_string):
	'''
	Performs Burrows-Wheeler transform

		Parameters:
			in_string (string): string to be transformed

		Returns:
			output (string): transformed string
	'''
	in_table = [in_string + bytes.fromhex('7F').decode('utf-8')]
	table = build_table(in_table)
	sorted_table = sort_table(table)
	output = extract_last_column(sorted_table) 
	return output 