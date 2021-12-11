import sys

'''
Module for performing forward Burrows-Wheeler transforms on python strings
'''

# Increase recursion limit
sys.setrecursionlimit(1000000)

def build_table(in_list):
	'''
	Returns a table (list) of strings. Each element in the list 
	contains the input text string shifted by the element's
	index

		Parameters:
			in_list (list): of length 1, contains string to be transformed

		Returns:
			in_list (list): of lenght len(in_list), table of rotated in_list
	'''
	# checks to see if in_list is fully built, i.e. the same length as 
	# the original string
	if len(in_list)<len(in_list[0]):
		# appends an element to in_list which is the string in the last
		#  element rotated by 1 character 
		in_list.append(in_list[-1][-1]+in_list[-1][0:-1])
		# recursive call to build_table()
		build_table(in_list)
	# if in_list is fully built, it is returned and program moves back
	# up through recursive calls
	return in_list	

def sort_table(table):
	'''
	Returns a lexicographically sorted a table (list) of strings
	'''
	table.sort()
	return table

def extract_last_column(table):
	'''
	Returns last column of table, i.e. the last characters in each
	element of table concatenated into a single string
	'''
	last_column = ''.join([table[i][-1] for i in range(len(table))]) 
	return last_column

def bwt(in_string):
	'''
	Performs Burrows-Wheeler transform. Processes input string and returns 
	transformed string
	'''
	# append an EOF character - chosen to be the last character in the ascii
	# table
	in_table = [in_string + '\x7f']
	table = build_table(in_table)
	sorted_table = sort_table(table)
	output = extract_last_column(sorted_table) 
	return output 