# -*- coding: utf-8 -*-
"""
Created on 2022-12-22

@author: afe02
"""

import unittest
import random
from collections import deque
import merge_array

class TestSort(unittest.TestCase):
    def testMerge(self):
        in_list1 = [1, 2, 5, 8, 9]
        in_list2 = [2, 3, 6, 7, 9]
        # correct size for output list
        merged_list1 = [0]*10
        merge_array.merge(in_list1, in_list2, merged_list1)
        merged_result = [1, 2, 2, 3, 5, 6, 7, 8, 9, 9]
        self.assertEqual(merged_list1, merged_result)
        self.assertEqual(in_list1, [1, 2, 5, 8, 9])
        self.assertEqual(in_list2, [2, 3, 6, 7, 9])
        in_list1 = [1, 2, 5, 8, 9]
        in_list2 = [2, 3, 6, 7, 9]
        # correct size for output list
        merged_list2 = [0]*10
        merge_array.merge(in_list2, in_list1, merged_list2)
        self.assertEqual(merged_list2, merged_result)
        self.assertEqual(in_list1, [1, 2, 5, 8, 9])
        self.assertEqual(in_list2, [2, 3, 6, 7, 9])

    def testSort(self):
        orig_list1 = random.sample(range(100), 100)
        orig_list2 = random.sample(range(100), 100)
        orig_list1.extend(orig_list2)
        merge_array.merge_sort(orig_list1)
        error_indices = []
        for i in range(100):
            ind1 = i*2
            if orig_list1[ind1] != i:
                error_indices.append(ind1)
            ind2 = ind1+1
            if orig_list1[ind2] != i:
                error_indices.append(ind2)
        self.assertEqual(error_indices, [])
 

if __name__ == '__main__':
    unittest.main()
