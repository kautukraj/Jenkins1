#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog11 import minList


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to find minimum in a list
        """
        data = [-1, -2, -10, 100]
        result = minList(data)
        self.assertEqual(result, -10)


if __name__ == '__main__':
    unittest.main()
