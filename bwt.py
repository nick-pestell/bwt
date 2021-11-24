import argparse

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

def run(in_file_path, out_file_path):
	try:
		with open(in_file_path, 'r') as fd:
			in_string = fd.read().rstrip()
	except FileNotFoundError as e:
		print(e)
	output = bwt(in_string)
	with open(out_file_path, 'w') as fd:
		fd.write(output)	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Burrows-Wheeler transfrom')
	parser.add_argument('in_file_path', metavar='Input file path', 
						help='path to input file')
	parser.add_argument('out_file_path', metavar='Output file path', 
						help='path to output file')
	args = parser.parse_args()
	run(args.in_file_path, args.out_file_path)