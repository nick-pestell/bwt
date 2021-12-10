import argparse
import sys
import errno

from bwt.transform import bwt
from bwt.inv_transform import inv_bwt

def run_forward(in_file_path, out_file_path):
	try:
		with open(in_file_path, 'r') as fd:
			in_string = fd.read()
	except FileNotFoundError as e:
		print(e)
		sys.exit(errno.ENOENT)
	output = bwt(in_string)
	with open(out_file_path, 'w') as fd:
		fd.write(output)	

def run_inverse(in_file_path, out_file_path):
	try: 
		with open(in_file_path, 'r') as fd:
			in_string = fd.read()
	except FileNotFoundError as e:
		print(e)
		sys.exit(errno.ENOENT)	
	output = inv_bwt(in_string)
	with open(out_file_path, 'w') as fd:
		fd.write(output)	

if __name__ == '__main__':
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