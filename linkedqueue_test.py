# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:08:56 2021

@author: afe02
"""

import unittest
import queue_linked_begin as linkedqueue

class TestConstructIsEmpty(unittest.TestCase):
    def testConstruction(self):
        lq = linkedqueue.LinkedQueue()
        self.assertIsNotNone(lq)
        self.assertTrue(lq.isEmpty())

class TestEnqueueFrontDequeueIsEmpty(unittest.TestCase):
    def testEnqueueFrontDequeueIsEmpty(self):
        lq = linkedqueue.LinkedQueue()
        lq.enqueue(4)
        self.assertFalse(lq.isEmpty())
        self.assertEqual(lq.front(), 4)
        self.assertFalse(lq.isEmpty())
        lq.enqueue(5)
        self.assertEqual(lq.front(), 4)
        self.assertEqual(lq.dequeue(), 4)
        self.assertEqual(lq.front(), 5)
        self.assertFalse(lq.isEmpty())
        self.assertEqual(lq.dequeue(), 5)
        self.assertTrue(lq.isEmpty())
        lq.enqueue(6)
        self.assertEqual(lq.front(), 6)
        self.assertEqual(lq.dequeue(), 6)
        self.assertTrue(lq.isEmpty())

class TestClear(unittest.TestCase):
    def testClear(self):
        lq = linkedqueue.LinkedQueue()
        lq.enqueue(4)
        lq.clear()
        self.assertTrue(lq.isEmpty())
        lq.enqueue(3)
        lq.enqueue(4)
        lq.enqueue(5)
        lq.clear()
        self.assertTrue(lq.isEmpty())
        
        

if __name__ == '__main__':
    unittest.main()
