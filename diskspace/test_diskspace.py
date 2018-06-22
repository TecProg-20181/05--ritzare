import unittest
import os
import re

from diskspace import *

class readable(unittest.TestCase):
    def test_type(self):
        bytes = bytes_to_readable(0)
        self.assertIsInstance(bytes, str)

    def test_size(self):
        bytes_size = bytes_to_readable(0)
        self.assertEqual(bytes_size, '0.00B')

    def test_size2(self):
        bytes_size = bytes_to_readable(2)
        self.assertEqual(bytes_size, '1.00Kb')

    def test_size3(self):
        bytes_size = bytes_to_readable(20000)
        self.assertEqual(bytes_size, '9.77Mb')

    def test_size4(self):
        bytes_size = bytes_to_readable(200000000)
        self.assertEqual(bytes_size, '95.37Gb')    

    def test_size5(self):
        bytes_size = bytes_to_readable(200000000000)
        self.assertEqual(bytes_size, '93.13Tb')        

    def test_bytes_not_none(self):
        bytes = bytes_to_readable(0)
        self.assertIsNotNone(bytes)

    def test_subprocess(self):
        command = 'du'
        result = subprocess_check_output(command)
        self.assertIsInstance(result, str)

    
if __name__ == '__main__':
    unittest.main()
        