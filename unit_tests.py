import unittest
from unittest import mock
import pickle as pkl
import argparse
import errno

from burrows_wheeler.transform import *
from burrows_wheeler.inv_transform import *
from bwt import * 

IN_FILE_PATH = 'test_files/turing.txt'
OUT_FILE_PATH = 'test_files/out_turing.txt'
TABLE_FILE_PATH = 'test_files/table.pkl'

class TestBwt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(IN_FILE_PATH, 'r') as fd:
            cls.in_string = fd.read()
        with open(OUT_FILE_PATH, 'r' ) as fd:
            cls.out_string = fd.read()
        with open(TABLE_FILE_PATH, 'rb') as fd:
            cls.table = pkl.load(fd)
        
    @classmethod
    def tearDownClass(cls):
        pass

class TestBwtForwardTransform(TestBwt):
    def test_build_transform_table(self):
        self.assertEqual(self.table, build_transform_table([self.in_string + '\x7f'])) 
        
    def test_bwt(self):
        self.assertEqual(bwt(self.in_string), self.out_string)

class TestBwtInverseTransfrom(TestBwt):
    def test_build_inv_table(self):
        self.assertEqual(len(self.out_string + '\x7f'), len(build_inv_table(self.out_string + '\x7f')))

    def test_extract_string(self):
        self.assertEqual(extract_string(self.table), self.in_string)

    def test_inv_bwt(self):
        self.assertEqual(inv_bwt(self.out_string), self.in_string)

class TestBwtInterface(TestBwt):
    def test_read_input_file(self):
        # test file not found
        with self.assertRaises(SystemExit) as context:
            read_input_file('foo.txt')
        self.assertEqual(context.exception.code, errno.ENOENT)
        # test succesful IO
        mock_open = mock.mock_open(read_data = 'success')
        with mock.patch('builtins.open', mock_open):
            self.assertEqual(read_input_file('foo.txt'), 'success')

    def test_run_forward(self):
        with mock.patch('bwt.read_input_file') as patch:
            patch.return_value = self.in_string 
            mock_open = mock.mock_open()
            with mock.patch('builtins.open', mock_open):
                run_forward('foo.txt', 'bar.txt')
                patch.assert_called_once_with('foo.txt')
                mock_open.assert_called_once_with('bar.txt', 'w')
                self.assertEqual(mock_open().write.call_args[0][0], self.out_string)

    def test_run_inverse(self):
        with mock.patch('bwt.read_input_file') as patch:
            patch.return_value = self.out_string 
            mock_open = mock.mock_open()
            with mock.patch('builtins.open', mock_open):
                run_inverse('foo.txt', 'bar.txt')
                patch.assert_called_once_with('foo.txt')
                mock_open.assert_called_once_with('bar.txt', 'w')
                self.assertEqual(mock_open().write.call_args[0][0], self.in_string)

def test_suit(test_objs):
    suit = unittest.TestSuite(test_objs)
    return suit
    
if __name__ == '__main__':
    forwd_bwt_tests = [TestBwtForwardTransform('test_build_transform_table'), TestBwtForwardTransform('test_bwt')]
    inv_bwt_test = [TestBwtInverseTransfrom('test_build_inv_table'), 
                    TestBwtInverseTransfrom('test_extract_string'),
                    TestBwtInverseTransfrom('test_inv_bwt')]
    interface_test = [TestBwtInterface('test_read_input_file'), TestBwtInterface('test_run_forward'),
                      TestBwtInterface('test_run_inverse')]
    runner = unittest.TextTestRunner()
    parser = argparse.ArgumentParser(description='Test code')
    type_arg = parser.add_argument('--type', '-t', nargs=1, 
                                   help='Forward or inverse transform', default=None)
    args = parser.parse_args()
    try:
        if args.type:
            if args.type[0] == 'forward':
                runner.run(test_suit(forwd_bwt_tests)) 
            elif args.type[0] == 'inverse':
                runner.run(test_suit(inv_bwt_test)) 
            elif args.type[0] == 'interface':
                runner.run(test_suit(interface_test)) 
            else:
                raise argparse.ArgumentError(type_arg, "Invalid argument. Please use 'forward', 'reverse' or 'interface'")
        else:
            unittest.main()
    except argparse.ArgumentError as e:
        print(e)
        sys.exit(errno.ENOENT)