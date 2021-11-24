import argparse
from transform import bwt

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