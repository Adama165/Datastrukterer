# -*- coding: utf-8 -*-
"""
TODO: implement recursiveCheckPalindrome

"""

def recursiveCheckPalindrome(word):
    # TODO implement
    # What is the base case? The base case is if the first and last letter of the word is the same.
    # How can we solve a small part of the problem check wether the first letter of the string is the same as the last
    # and call recursiveCheckPalindrome with a subset of the
    # initial problem?
    # Use lower() to make the method case insensitive
    # return True if word is a palindrome, False otherwise
    word = word.lower() #Makes the word lowercase
    if len(word) < 2:   #Checks if the word is longer than 2 characters
        return True     # if it is then it is a palindrome and returns true
    if word[0] != word[-1]: #Checks if the first character in the word does not match the last character in the word
        return False    #If it does not match then return false
    return recursiveCheckPalindrome(word[1:-1]) # If both checks are not "cleared" then the word
                                                # is returned again to the function with one character
                                                # taken away from the word both in front and in the back
                                                # to recursively check if the word is a palindrome or not.


