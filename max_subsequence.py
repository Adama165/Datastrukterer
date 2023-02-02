# -*- coding: utf-8 -*-
"""
Anna Friebe for DVA45

Three different functions that find the maximum sum within a 
contiguous subsequence of the list S

@author: afe02
"""

def max_subsequence1(S):
    maxSum = 0
    # iterate through all possible left indices for subsequences
    for i in range(len(S)):
        # iterate trough all possible right indices for subsequences
        for j in range(i, len(S)):
            # sum from i to j
            testSum = 0
            for k in range(i, j+1):
                testSum += S[k]
            if testSum > maxSum:
                # store if largest so far
                maxSum = testSum
    return maxSum


def max_subsequence2(S):
    maxSum = 0
    # iterate through all possible left indices for subsequences
    for i in range(len(S)):
        # iterate trough all possible right indices for subsequences,
        # while summing the values
        testSum = 0
        for j in range(i, len(S)):
            # sum from i to j
            testSum += S[j]
            if testSum > maxSum:
                # store if largest so far
                maxSum = testSum
    return maxSum


# This version is more tricky to understand.
# We don't need to test all possible left indices - if a sum from i-j is > 0
# it is always better to start from i compared to j. But once we have a 
# negative accumulated sum we should start a new subsequence 
# (test a new left index).
def max_subsequence3(S):
    maxSum = 0
    testSum = 0
    # iterate through the list
    for i in range(len(S)):
        # sum (test all possible right indices of the list)
        testSum += S[i]
        if testSum > maxSum:
            # store if largest so far
            maxSum = testSum
        # if negative we start with a new left index
        if testSum < 0:
            testSum = 0
    return maxSum
