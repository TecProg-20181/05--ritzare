import unittest
import os
import re

from diskspace import bytes_to_readable

class readable(unittest.TestCase):
    def test_type(self):
        bytes = bytes_to_readable(0)
        self.assertIsInstance(bytes, str)

    def test_size(self):
        bytes_size = bytes_to_readable(0)
        self.assertEqual(bytes_size, '0.00B')


if __name__ == '__main__':
    unittest.main()
        