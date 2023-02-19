# -*- coding: utf-8 -*-
"""
Created on 2022-12-22

@author: afe02
"""

import unittest
import random
from collections import deque
import merge_queue_begin as merge_queue

class TestSort(unittest.TestCase):
    def testMerge(self):
        in_queue1 = deque([1, 2, 5, 8, 9])
        in_queue2 = deque([2, 3, 6, 7, 9])
        merged_queue1 = merge_queue.merge(in_queue1, in_queue2)
        merged_result = deque([1, 2, 2, 3, 5, 6, 7, 8, 9, 9])
        self.assertEqual(merged_queue1, merged_result)
        self.assertEqual(in_queue1, deque([]))
        self.assertEqual(in_queue2, deque([]))
        in_queue1 = deque([1, 2, 5, 8, 9])
        in_queue2 = deque([2, 3, 6, 7, 9])
        merged_queue2 = merge_queue.merge(in_queue2, in_queue1)
        self.assertEqual(merged_queue2, merged_result)
        self.assertEqual(in_queue1, deque())
        self.assertEqual(in_queue2, deque())

    def testMergeLevelQueues(self):
        in_queue1 = deque([1, 2, 5, 8, 9])
        in_queue2 = deque([2, 3, 6, 7, 9])
        in_queue3 = deque([3, 4, 8])
        in_queue4 = deque([3, 6, 7, 9])
        in_queue5 = deque([1, 4, 8])
        in_level_queues = deque([in_queue1, in_queue2, in_queue3, in_queue4, in_queue5])
        next_level_queues = merge_queue.merge_level_queues(in_level_queues)
        self.assertEqual(len(next_level_queues), 3)
        self.assertEqual(next_level_queues[0], deque([1, 2, 2, 3, 5, 6, 7, 8, 9, 9]))
        self.assertEqual(next_level_queues[1], deque([3, 3, 4, 6, 7, 8, 9]))
        self.assertEqual(next_level_queues[2], deque([1, 4, 8])) 
        self.assertEqual(in_level_queues, deque())

    def testSort(self):
        input_queue = deque()
        orig_list1 = random.sample(range(100), 100)
        orig_list2 = random.sample(range(100), 100)
        input_queue = deque(orig_list1)
        input_queue.extend(orig_list2)
        merge_sort_queue = merge_queue.merge_sort(input_queue)
        error_indices = []
        for i in range(100):
            if merge_sort_queue.popleft() != i:
                error_indices.append(i*2)
            if merge_sort_queue.popleft() != i:
                error_indices.append(i*2+1)
        self.assertEqual(error_indices, [])
 

if __name__ == '__main__':
    unittest.main()
