# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:25:04 2021

@author: afe02
"""
import unittest
import checkPalindrome



class CheckPalindromeTest(unittest.TestCase):
    def testPalindrome(self):
        self.assertTrue(checkPalindrome.recursiveCheckPalindrome("Apa"))
        self.assertFalse(checkPalindrome.recursiveCheckPalindrome("Myra"))
        self.assertTrue(checkPalindrome.recursiveCheckPalindrome("Naturrutan"))
        
        
if __name__ == '__main__':
    unittest.main()
    