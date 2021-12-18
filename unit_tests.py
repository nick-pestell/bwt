import unittest
import pickle as pkl
import argparse
import errno

from bwt.transform import *
from bwt.inv_transform import *

IN_FILE_PATH = 'test_files/turing.txt'
OUT_FILE_PATH = 'test_files/out_turing.txt'
TABLE_FILE_PATH = 'test_files/table.pkl'

class TestBwtTransform(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBwtTransform, self).__init__(*args, **kwargs)
        with open(IN_FILE_PATH, 'r') as fd:
            self.in_string = fd.read()
        with open(OUT_FILE_PATH, 'r' ) as fd:
            self.out_string = fd.read()
        with open(TABLE_FILE_PATH, 'rb') as fd:
            self.table = pkl.load(fd)

    def test_build_transform_table(self):
        self.assertEqual(self.table, build_transform_table([self.in_string + '\x7f'])) 
        
    def test_bwt(self):
        self.assertEqual(bwt(self.in_string), self.out_string)

class TestBwtInverseTransfrom(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBwtInverseTransfrom, self).__init__(*args, **kwargs)
        with open(IN_FILE_PATH, 'r') as fd:
            self.in_string = fd.read()
        with open(OUT_FILE_PATH, 'r' ) as fd:
            self.out_string = fd.read()
        with open(TABLE_FILE_PATH, 'rb') as fd:
            self.table = pkl.load(fd)

    def test_build_inv_table(self):
        self.assertEqual(len(self.out_string + '\x7f'), len(build_inv_table(self.out_string + '\x7f')))

    def test_extract_string(self):
        self.assertEqual(extract_string(self.table), self.in_string)

    def test_inv_bwt(self):
        self.assertEqual(inv_bwt(self.out_string), self.in_string)

def test_suit(test_objs):
    suit = unittest.TestSuite(test_objs)
    return suit
    
if __name__ == '__main__':
    bwt_tests = [TestBwtTransform('test_build_transform_table'), TestBwtTransform('test_bwt')]
    inv_bwt_test = [TestBwtInverseTransfrom('test_build_inv_table'), 
                    TestBwtInverseTransfrom('test_extract_string'),
                    TestBwtInverseTransfrom('test_inv_bwt')]
    runner = unittest.TextTestRunner()
    parser = argparse.ArgumentParser(description='Test code')
    type_arg = parser.add_argument('--type', '-t', nargs=1, 
                                   help='Forward or inverse transform', default=None)
    args = parser.parse_args()
    try:
        if args.type:
            if args.type[0] == 'forward':
                runner.run(test_suit(bwt_tests)) 
            elif args.type[0] == 'inverse':
                runner.run(test_suit(inv_bwt_test)) 
            else:
                raise argparse.ArgumentError(type_arg, "Invalid argument. Please use 'forward' or 'reverse'")
        else:
            unittest.main()
    except argparse.ArgumentError as e:
        print(e)
        sys.exit(errno.EINVAL)