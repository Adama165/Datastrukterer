# 
# For DVA245 by Anna Friebe, January 2023 

from collections import deque
import random


def merge(S1, S2):
    """Merge two sorted queue instances S1 and S2.
       Result is returned in a new sorted queue.
       Leaves S1 and S2 empty.
       Queues are deques used with the front to the left."""
    S = deque()
    # TODO add the functionality that merges S1 and S2 into S
    while 0 < len(S1) and 0 < len(S2):
        if S1[0] < S2[0]:
            add = S1.popleft()
            S.append(add)
        else:
            add = S2.popleft()
            S.append(add)
    S += S1
    S1.clear()
    S += S2
    S2.clear()
    
    return S
  
def merge_level_queues(level_queues):
    """Merge the sorted queues in level_queues two by two
    into a new queue with about half the number of sorted 
    queues. level_queues is left empty."""
    next_level_queues = deque()
    # TODO add the functionality that merges the queues of level_queues
    # into next_level_queues
    while len(level_queues) > 1:
        q1 = level_queues.popleft()
        q2 = level_queues.popleft()
        next_level_queues.append(merge(q1,q2))
    if len(level_queues) > 0:
        next_level_queues.append(level_queues.popleft())
    return next_level_queues
  

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm.
    The sorted result is returned in a new queue, S is left empty
    Queues are deques used with the front to the left. """
    level_queues = deque()
    # TODO: Create a queue for each input element and add them to the level_queues
    for i in range(len(S)):
        element = S.popleft()
        q1 = deque()
        q1.append(element)
        level_queues.append(q1)
    # TODO: while we have more than one queue remaining, merge a level 
    while len(level_queues) > 1:
        level_queues = merge_level_queues(level_queues)
    sorted_level_queues = level_queues.popleft()
    return sorted_level_queues
    # TODO: dequeue and return the single remaining merged queue





#myqueue1 = deque([1,3,6,7,9])
#myqueue2 = deque([2,8,9,10,11])
#myqueue1 = deque([1, 2, 5, 8, 9])
#myqueue2 = deque([2, 3, 6, 7, 9])
""" in_queue1 = deque([1, 2, 5, 8, 9])
in_queue2 = deque([2, 3, 6, 7, 9])
in_queue3 = deque([3, 4, 8])
in_queue4 = deque([3, 6, 7, 9])
in_queue5 = deque([1, 4, 8]) """
#print(myqueue1)
#print(myqueue2)

#print("merged",merge(myqueue1, myqueue2))

""" in_level_queues = deque([in_queue1, in_queue2, in_queue3, in_queue4, in_queue5])
next_level_queues = merge_level_queues(in_level_queues)
print(next_level_queues) """

input_queue = deque()
orig_list1 = random.sample(range(100), 100)
orig_list2 = random.sample(range(100), 100)
input_queue = deque(orig_list1)
input_queue.extend(orig_list2)
print(input_queue)
merge_sort_queue = merge_sort(input_queue)
