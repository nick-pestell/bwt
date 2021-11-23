import argparse

def bwt(in_string):
	table = [in_string]
	return build_table(table)

def build_table(in_list):
	in_list.append(in_list[-1][-1]+in_list[-1][0:-1])
	if len(in_list)==len(in_list[0]):
		return in_list	
	return build_table(in_list)

def run(in_file_path, out_file_path):
	try:
		with open(in_file_path, 'r') as fd:
			in_string = fd.read().rstrip()
	except FileNotFoundError as e:
		print(e)
	with open(out_file_path, 'w') as fd:
		fd.write('\n'.join(bwt(in_string)))	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Burrows-Wheeler transfrom')
	parser.add_argument('in_file_path', metavar='Input file path', 
						help='path to input file')
	parser.add_argument('out_file_path', metavar='Output file path', 
						help='path to output file')
	args = parser.parse_args()
	run(args.in_file_path, args.out_file_path)