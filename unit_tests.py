import unittest
import pickle as pkl

from bwt.transform import *
from bwt.inv_transform import *

TEST_IN_STRING = 'hello world!\n'
TEST_OUT_STRING = '!odlh\x7frellwo \n'
TEST_OUT_TABLE = ['\n\x7fhello world!', 
                  ' world!\n\x7fhello', 
                  '!\n\x7fhello world', 
                  'd!\n\x7fhello worl', 
                  'ello world!\n\x7fh', 
                  'hello world!\n\x7f', 
                  'ld!\n\x7fhello wor', 
                  'llo world!\n\x7fhe', 
                  'lo world!\n\x7fhel', 
                  'o world!\n\x7fhell', 
                  'orld!\n\x7fhello w', 
                  'rld!\n\x7fhello wo', 
                  'world!\n\x7fhello ', 
                  '\x7fhello world!\n']
IN_FILE_PATH = './test_files/turing.txt'
OUT_FILE_PATH = './test_files/out_turing.txt'
TABLE_FILE_PATH = './test_files/table.pkl'

class TestBwtTransform(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBwtTransform, self).__init__(*args, **kwargs)
        with open(IN_FILE_PATH, 'w') as fd:
            self.in_string = fd.read()
        with open(OUT_FILE_PATH, 'w' ) as fd:
            self.out_string = fd.read()
        with open(TABLE_FILE_PATH, 'rb') as fd:
            self.table = pkl.load(fd)

    def test_build_transform_table(self):
        self.assertListEqual(self.table, build_transform_table([self.in_string])) 
        
    def test_bwt(self):
        self.assertEqual(bwt(self.in_string), self.out_string)

    def test_build_inv_table(self):
        self.assertEqual(len(self.out_string), len(build_inv_table(self.out_string)))

    def test_extract_string(self):
        self.assertEqual(extract_string(self.table), self.in_string)

    def test_inv_bwt(self):
        self.assertEqual(inv_bwt(self.out_string), self.in_string)

