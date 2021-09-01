# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 20:45:54 2021

@author: user
"""

#God
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


        if len(s) <= 1:
            return s

        charMap = dict()
        start = 0
        longest = 0
        
        for i,c in enumerate(s):
            if c in charMap:
                start = max(start, charMap[c]+1)
            longest = max(longest, i-start+1)
            charMap[c] = i
        
        return longest