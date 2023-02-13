# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:08:56 2021

@author: afe02
"""

import unittest
import stack_linked_begin as linkedstack

class TestConstructIsEmpty(unittest.TestCase):
    def testConstruction(self):
        ls = linkedstack.LinkedStack()
        self.assertIsNotNone(ls)
        self.assertTrue(ls.isEmpty())

class TestPushTopPopIsEmpty(unittest.TestCase):
    def testPushTopPopIsEmpty(self):
        ls = linkedstack.LinkedStack()
        ls.push(4)
        self.assertFalse(ls.isEmpty())
        self.assertEqual(ls.top(), 4)
        self.assertFalse(ls.isEmpty())
        ls.push(5)
        self.assertEqual(ls.top(), 5)
        self.assertEqual(ls.pop(), 5)
        self.assertEqual(ls.top(), 4)
        self.assertFalse(ls.isEmpty())
        self.assertEqual(ls.pop(), 4)
        self.assertTrue(ls.isEmpty())
        ls.push(6)
        self.assertEqual(ls.top(), 6)
        self.assertEqual(ls.pop(), 6)
        self.assertTrue(ls.isEmpty())

class TestClear(unittest.TestCase):
    def testClear(self):
        ls = linkedstack.LinkedStack()
        ls.push(4)
        ls.clear()
        self.assertTrue(ls.isEmpty())
        ls.push(3)
        ls.push(4)
        ls.push(5)
        ls.clear()
        self.assertTrue(ls.isEmpty())
        
        

if __name__ == '__main__':
    unittest.main()
