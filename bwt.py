import argparse
import sys
import errno

from burrows_wheeler.transform import bwt
from burrows_wheeler.inv_transform import inv_bwt

def read_input_file(in_file_path):
	try:
		with open(in_file_path, 'r') as fd:
			in_string = fd.read()
	except FileNotFoundError as e:
		print(e)
		sys.exit(errno.ENOENT)
	return in_string

def run_forward(in_file_path, out_file_path):
	in_string = read_input_file(in_file_path)	
	output = bwt(in_string)
	with open(out_file_path, 'w') as fd:
		fd.write(output)	

def run_inverse(in_file_path, out_file_path):
	in_string = read_input_file(in_file_path)	
	output = inv_bwt(in_string)
	with open(out_file_path, 'w') as fd:
		fd.write(output)	
		
def main():
	parser = argparse.ArgumentParser(description='Burrows-Wheeler transfrom')
	parser.add_argument('--inv', dest='run', action='store_const',
						const=run_inverse, default=run_forward,
						help='run inverse BWT (default: run fordwars BWT')
	parser.add_argument('in_file_path', metavar='Input file path', 
						help='path to input file')
	parser.add_argument('out_file_path', metavar='Output file path', 
						help='path to output file')
	args = parser.parse_args()
	args.run(args.in_file_path, args.out_file_path)

if __name__ == '__main__':
	main()