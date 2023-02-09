# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:08:56 2021

@author: afe02
"""

import unittest
import linkedlist_begin as linkedlist

class TestConstructNoArgLinkedList(unittest.TestCase):
    def testConstruction(self):
        ll = linkedlist.LinkedList()
        self.assertIsNotNone(ll)
        self.assertEqual(len(ll), 0)

class TestAppendGetItemLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = linkedlist.LinkedList()
    def testAppendGetItem(self):
        for i in range(100):
            self.ll.append(i)
        for i in range(100):
            self.assertEqual(self.ll[i], i)

class TestConstructArgEqualityIterLinkedList(unittest.TestCase):
    def testConstructionArgumentEquality(self):
        ll = linkedlist.LinkedList()
        for i in range(3):
            ll.append(i)
        # construct a copy
        llc = linkedlist.LinkedList(ll)
        self.assertEqual(ll, llc)
        ll.append(300)
        self.assertNotEqual(ll, llc)
        for i in range(3):
            self.assertEqual(llc[i], i)

class TestAddDelItemContainsInsertSetItemIterLinkedList(unittest.TestCase):
    def setUp(self):
        self.l1 = linkedlist.LinkedList()
        for i in range(100):
            self.l1.append(i)
        self.l2 = linkedlist.LinkedList()
        for i in range(50):
            self.l2.append(i+100)
        self.l3 = linkedlist.LinkedList()
        for i in range(100):
            self.l3.append(i)
    def testAdd(self):
        sumll = self.l1 + self.l2
        for i in range(150):
            self.assertEqual(sumll[i], i)
    def testDelItemContainsLen(self):
        del self.l1[1]
        self.assertFalse(1 in self.l1)
        self.assertEqual(self.l1[0], 0)
        self.assertEqual(self.l1[1], 2)
        self.assertEqual(len(self.l1), 99)
        self.assertNotEqual(self.l1, self.l3)
        del self.l1[0]
        self.assertFalse(0 in self.l1)
        self.assertEqual(len(self.l1), 98)
        self.assertEqual(self.l1[0], 2)
        self.assertEqual(self.l1[1],3)
        del self.l1[97]
        self.assertFalse(99 in self.l1)
        self.assertEqual(len(self.l1), 97)
        self.assertEqual(self.l1[96], 98)
        # check that append still works
        self.l1.append(99)
        self.assertTrue(99 in self.l1)
        self.assertEqual(self.l1[97], 99)
    def testInsert(self):
        self.l1.insert(1000, 333)
        self.l3.append(333)
        self.assertEqual(self.l1, self.l3)
        self.l1.insert(0, 222)
        self.assertEqual(len(self.l1), 102)
        self.assertEqual(self.l1[0], 222)
        self.l3.insert(5, 111)
        self.assertEqual(self.l3[5], 111)
        self.assertEqual(self.l3[4], 4)
        self.assertEqual(self.l3[6], 5)
    def testSetItemContains(self):
        self.l1[0] = 111
        self.l1[99] = 222
        self.l1[50] = 333
        self.assertEqual(self.l1[0], 111)
        self.assertEqual(self.l1[99], 222)
        self.assertEqual(self.l1[50], 333)
        self.assertFalse(0 in self.l1)
        self.assertFalse(99 in self.l1)
        self.assertFalse(50 in self.l1)
    def testIter(self):
        i = 0
        for item in self.l1:
            self.assertEqual(item, i)
            i += 1
        self.assertEqual(i, 100)

if __name__ == '__main__':
    unittest.main()
