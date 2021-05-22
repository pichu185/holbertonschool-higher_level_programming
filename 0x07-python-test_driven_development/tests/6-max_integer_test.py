#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    ''' Test positive output'''
    def positives(self):
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([0],0)
        self.assertEqual([4, 3, 2, 1], 4)
        self.assertEqual([7, 7, 7, 7], 7)

    ''' Test negative output'''
    def negatives(self):
        self.assertEqual([-1, -2, -3, -4], -1)
        self.assertEqual([-4, -3, -2, -1], -1)
        self.assertEqual([-1], -1)
    
if __name__ == '__main__':
    unittest.main()