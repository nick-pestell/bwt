def build_table(in_list):
	if len(in_list)<len(in_list[0]):
		in_list.append(in_list[-1][-1]+in_list[-1][0:-1])
		build_table(in_list)
	return in_list	

def sort_table(table):
	table.sort()
	return table

def extract_last_column(table):
	return ''.join([table[i][-1] for i in range(len(table))])

def bwt(in_string):
	in_table = [in_string]
	table = build_table(in_table)
	sorted_table = sort_table(table)
	return extract_last_column(sorted_table)

def i_btw(out_string):
	pass