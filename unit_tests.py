import unittest

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

class TestBwtTransform(unittest.TestCase):
    def test_build_table(self):
        self.assertEqual(len(TEST_IN_STRING), len(build_table([TEST_IN_STRING]))) 
        
    def test_bwt(self):
        self.assertEqual(bwt(TEST_IN_STRING), TEST_OUT_STRING)

    def test_build_table(self):
        self.assertEqual(len(TEST_OUT_STRING), len(build_table(TEST_OUT_STRING)))

    def test_extract_string(self):
        self.assertEqual(extract_string(TEST_OUT_TABLE), TEST_IN_STRING)

    def test_inv_bwt(self):
        self.assertEqual(inv_bwt(TEST_OUT_STRING), TEST_IN_STRING)