# 
# For DVA245 by Anna Friebe, January 2023 

from collections import deque


def merge(S1, S2):
    """Merge two sorted queue instances S1 and S2.
       Result is returned in a new sorted queue.
       Leaves S1 and S2 empty.
       Queues are deques used with the front to the left."""
    S = deque()
    # TODO add the functionality that merges S1 and S2 into S
    index = 0
    while index < len(S1) and index < len(S2):
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
    return next_level_queues
  

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm.
    The sorted result is returned in a new queue, S is left empty
    Queues are deques used with the front to the left. """
    level_queues = deque()
    # TODO: Create a queue for each input element and add them to the level_queues
    # TODO: while we have more than one queue remaining, merge a level 
    # TODO: dequeue and return the single remaining merged queue

#myqueue1 = deque([1,3,6,7,9])
#myqueue2 = deque([2,8,9,10,11])
myqueue1 = deque([1, 2, 5, 8, 9])
myqueue2 = deque([2, 3, 6, 7, 9])

print(myqueue1)
print(myqueue2)

print("merged",merge(myqueue1, myqueue2))
